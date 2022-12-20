from functools import reduce
from typing import Callable, Tuple

from sql_smith.interfaces import EngineInterface, StatementInterface
from sql_smith.query import SelectQuery, UpdateQuery, DeleteQuery, InsertQuery


class BasicEngine(EngineInterface):
    """Basic engine

    A default implementation of an engine.
    """
    def make_select(self) -> 'SelectQuery':
        """Creates a SelectQuery."""
        return SelectQuery(self)

    def make_insert(self) -> 'InsertQuery':
        """Creates an InsertQuery."""
        return InsertQuery(self)

    def make_update(self) -> 'UpdateQuery':
        """Creates an UpdateQuery."""
        return UpdateQuery(self)
    
    def make_delete(self) -> 'DeleteQuery':
        """Creates a DeleteQuery."""
        return DeleteQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        """Escapes an identifier.

        The default implementation returns the identifier as is.
        """
        return identifier

    def escape_like(self, parameter: str) -> str:
        """Escapes the LIKE argument

        A backslash is used to escape wildcards.
        Standard wildcards are underscore and percent sign.
        """
        return parameter.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_')

    def export_parameter(self, param) -> str:
        """Export a parameter.

        A boolean will be exported as true or false. A None value will be exported as NULL.
        """
        if isinstance(param, bool):
            return 'true' if param else 'false'
        if param is None:
            return 'NULL'
        return str(param)

    def extract_params(self) -> Callable[['StatementInterface'], Tuple]:
        """Create a lambda to extract parameters."""
        return lambda statement: statement.params(self)

    def extract_sql(self) -> Callable[['StatementInterface'], str]:
        """Create a lambda to extract SQL."""
        return lambda statement: statement.sql(self)

    def flatten_params(self, *args: 'StatementInterface') -> Tuple:
        """Create a tuple with all parameters found."""
        # map with extract_params returns a list with tuples,
        # the reduce method is used to merge all these tuples into one big tuple
        return reduce(lambda x, y: (x + y), map(self.extract_params(), args), ())

    def flatten_sql(self, separator: str, *args: 'StatementInterface') -> str:
        """Transform StatementInterface arguments to a string."""
        return separator.join(list(map(self.extract_sql(), args)))

    def get_parameter_placeholder(self):
        return '?'
