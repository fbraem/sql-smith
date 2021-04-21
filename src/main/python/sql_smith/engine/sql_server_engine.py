from sql_smith.engine import BasicEngine
from sql_smith.query.sql_server.select_query import SelectQuery
from sql_smith.query.sql_server.delete_query import DeleteQuery


class SqlServerEngine(BasicEngine):
    def make_select(self) -> 'SelectQuery':
        return SelectQuery(self)

    def make_delete(self) -> 'DeleteQuery':
        return DeleteQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        return '[{}]'.format(identifier)

    def escape_like(self, parameter: str) -> str:
        return super().escape_like(parameter).replace('[', r'\[').replace(']', r'\]')
