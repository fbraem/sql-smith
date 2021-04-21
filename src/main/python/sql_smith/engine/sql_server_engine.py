from sql_smith.engine import BasicEngine
from sql_smith.query.sql_server.select_query import SelectQuery
from sql_smith.query.sql_server.delete_query import DeleteQuery


class SqlServerEngine(BasicEngine):
    """A custom engine for SQL Server SQL dialect."""
    def make_select(self) -> 'SelectQuery':
        """Creates a custom SQL Server SELECT query.

        SQL Server handles OFFSET and LIMIT differently.
        """
        return SelectQuery(self)

    def make_delete(self) -> 'DeleteQuery':
        """Creates a custom SQL Server DELETE query.

        SQL Server handles LIMIT differently.
        """
        return DeleteQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        """Escapes identifiers with brackets."""
        return '[{}]'.format(identifier)

    def escape_like(self, parameter: str) -> str:
        """Escape like argument.

        Also escapes character ranges.
        """
        return super().escape_like(parameter).replace('[', r'\[').replace(']', r'\]')
