from typing import Tuple, Union

from sql_smith.partial.parameter import NullParameter, BoolParameter
from sql_smith.interfaces import StatementInterface


class Parameter(StatementInterface):
    def __init__(self, value: Union[str, int, float]):
        self._params = (value, )

    @classmethod
    def create(cls, value) -> StatementInterface:
        if value is None:
            return NullParameter()
        if isinstance(value, bool):
            return BoolParameter(value)

        return Parameter(value)

    def sql(self, engine: 'EngineInterface') -> str:
        return engine.export_parameter(engine.get_parameter_placeholder())

    def params(self, engine: 'EngineInterface') -> Tuple:
        return self._params
