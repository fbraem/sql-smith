from sql_smith.engine import BasicEngine


class CommonEngine(BasicEngine):
    """An engine that supports common SQL standard."""
    def escape_identifier(self, identifier: str) -> str:
        """Escapes identifiers by putting quotes around it."""
        return '"{}"'.format(identifier)
