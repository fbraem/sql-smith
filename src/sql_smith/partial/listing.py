from typing import Tuple

from sql_smith.interfaces import StatementInterface


class Listing(StatementInterface):
    def __init__(self, separator: str, *statements: 'StatementInterface'):
        self._separator = separator
        self._statements = statements

    def sql(self, engine: 'EngineInterface') -> str:
        return engine.flatten_sql(self._separator, *self._statements)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return engine.flatten_params(*self._statements)
