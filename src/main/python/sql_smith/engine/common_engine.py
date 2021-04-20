from sql_smith.engine import BasicEngine


class CommonEngine(BasicEngine):
    def escape_identifier(self, identifier: str) -> str:
        return '"{}"'.format(identifier)
