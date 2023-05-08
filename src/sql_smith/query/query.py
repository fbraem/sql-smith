class Query:
    """The result of a compile."""

    def __init__(self, sql: str, params: tuple):
        self._sql = sql
        self._params = params

    @property
    def sql(self) -> str:
        """Returns the compiled SQL statement as a string."""
        return self._sql

    @property
    def params(self) -> tuple:
        """Returns all parameters of the SQL statement."""
        return self._params
