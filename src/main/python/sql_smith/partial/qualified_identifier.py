from typing import Tuple

from sql_smith.interfaces import StatementInterface


class QualifiedIdentifier(StatementInterface):
    def __init__(self, *args: Tuple['StatementInterface']):
        self._identifiers = args

    def sql(self, engine: 'EngineInterface') -> str:
        return engine.flatten_sql('.', *self._identifiers)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return engine.flatten_params(*self._identifiers)
