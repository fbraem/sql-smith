from typing import Tuple

from sql_smith.interfaces import StatementInterface


class NullParameter(StatementInterface):
    def sql(self, engine: 'EngineInterface') -> str:
        return engine.export_parameter(None)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return ()
