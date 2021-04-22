from typing import Tuple


class Query:
    def __init__(self, sql: str, params: Tuple):
        self._sql = sql
        self._params = params

    @property
    def sql(self) -> str:
        return self._sql

    @property
    def params(self) -> Tuple:
        return self._params
