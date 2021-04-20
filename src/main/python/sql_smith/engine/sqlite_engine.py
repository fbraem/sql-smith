from sql_smith.engine import BasicEngine


class SqliteEngine(BasicEngine):
    def export_parameter(self, param) -> str:
        # SQLite doesn't have a boolean storage class, so 1/0 is used
        if type(param) == bool:
            return str(int(param))
        return super().export_parameter(param)
