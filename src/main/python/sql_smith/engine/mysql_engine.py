from sql_smith.engine import BasicEngine
from sql_smith.query.mysql import SelectQuery, InsertQuery


class MysqlEngine(BasicEngine):
    def make_select(self) -> 'SelectQuery':
        return SelectQuery(self)

    def make_insert(self) -> 'InsertQuery':
        return InsertQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        return '`{}`'.format(identifier)
