from typing import List


class Query:
    def __init__(self, sql: str, params: List):
        self._sql = sql
        self._params = params

    @property
    def sql(self) -> str:
        return self._sql

    @property
    def params(self) -> List:
        return self._params
