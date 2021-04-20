from sql_smith.engine import CommonEngine
from sql_smith.query.postgres import InsertQuery, UpdateQuery


class PostgresEngine(CommonEngine):
    def make_insert(self) -> 'InsertQuery':
        return InsertQuery(self)

    def make_update(self) -> 'UpdateQuery':
        return UpdateQuery(self)
