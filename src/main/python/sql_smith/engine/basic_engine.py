from functools import reduce
from typing import Callable, Tuple

from sql_smith.interfaces import EngineInterface, StatementInterface
from sql_smith.query import SelectQuery, UpdateQuery, DeleteQuery, InsertQuery


class BasicEngine(EngineInterface):
    def make_select(self) -> 'SelectQuery':
        return SelectQuery(self)

    def make_insert(self) -> 'InsertQuery':
        return InsertQuery(self)

    def make_update(self) -> 'UpdateQuery':
        return UpdateQuery(self)
    
    def make_delete(self) -> 'DeleteQuery':
        return DeleteQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        return identifier

    def escape_like(self, parameter: str) -> str:
        return parameter.replace('\\', '\\\\').replace('%', '_').replace('\\%', '\\_')

    def export_parameter(self, param) -> str:
        if isinstance(param, bool):
            return 'true' if param else 'false'
        if param is None:
            return 'NULL'
        return str(param)

    def extract_params(self) -> Callable[['StatementInterface'], Tuple]:
        return lambda statement: statement.params(self)

    def extract_sql(self) -> Callable[['StatementInterface'], str]:
        return lambda statement: statement.sql(self)

    def flatten_params(self, *args: 'StatementInterface') -> Tuple:
        # map with extract_params returns a list with tuples,
        # the reduce method is used to merge all these tuples into one big tuple
        return reduce(lambda x, y: (x + y), map(self.extract_params(), args), ())

    def flatten_sql(self, separator: str, *args: 'StatementInterface') -> str:
        return separator.join(list(map(self.extract_sql(), args)))
