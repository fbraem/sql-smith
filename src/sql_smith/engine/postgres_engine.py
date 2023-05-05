from sql_smith.engine import CommonEngine
from sql_smith.query.postgres import InsertQuery, UpdateQuery


class PostgresEngine(CommonEngine):
    """A custom engine for Postgres SQL dialect."""
    def make_insert(self) -> 'InsertQuery':
        """Creates a custom Postgres INSERT query.

        The Postgres insert query supports RETURNING.
        """
        return InsertQuery(self)

    def make_update(self) -> 'UpdateQuery':
        """Creates a custom Postgres INSERT query.

        The Postgres update query supports RETURNING.
        """
        return UpdateQuery(self)

    def get_parameter_placeholder(self):
        return '%s'
