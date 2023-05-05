from typing import Tuple

from sql_smith.interfaces import StatementInterface


class Literal(StatementInterface):
    def __init__(self, value):
        self._value = value

    def sql(self, engine: 'EngineInterface') -> str:
        return str(self._value)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return ()

