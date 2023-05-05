from sql_smith.engine import BasicEngine
from sql_smith.query.mysql import SelectQuery, InsertQuery


class MysqlEngine(BasicEngine):
    """A custom engine for MySQL SQL dialect."""
    def make_select(self) -> 'SelectQuery':
        """Creates a custom MySql SELECT query.

        The MySQL select query supports SQL_CALC_FOUND_ROWS.
        """
        return SelectQuery(self)

    def make_insert(self) -> 'InsertQuery':
        """Creates a custom MySql INSERT query.

        The MySQL insert query supports IGNORE.
        """
        return InsertQuery(self)

    def escape_identifier(self, identifier: str) -> str:
        """Escapes the identifier by surrounding it with backticks."""
        return '`{}`'.format(identifier)

    def get_parameter_placeholder(self):
        return '%s'
