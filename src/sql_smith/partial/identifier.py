from typing import Tuple

from sql_smith.interfaces import StatementInterface


class Identifier(StatementInterface):
    def __init__(self, name: str):
        self._name = name

    def sql(self, engine: 'EngineInterface') -> str:
        return engine.escape_identifier(self._name)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return ()
