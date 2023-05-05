from sql_smith.engine import BasicEngine


class SqliteEngine(BasicEngine):
    """A custom engine for Sqlite SQL dialect."""
    def export_parameter(self, param) -> str:
        """Export a parameter.

        SQLite doesn't support boolean storage class.
        True is translated to 1, False to 0.
        """
        if type(param) == bool:
            return str(int(param))
        return super().export_parameter(param)
