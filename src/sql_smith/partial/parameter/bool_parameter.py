from typing import Tuple

from sql_smith.interfaces import StatementInterface


class BoolParameter(StatementInterface):
    def __init__(self, value: bool):
        self._value = value

    def sql(self, engine: 'EngineInterface') -> str:
        return engine.export_parameter(self._value)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return ()
