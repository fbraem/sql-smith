from typing import Tuple

from sql_smith.interfaces import ExpressionInterface, EngineInterface


class Expression(ExpressionInterface):
    def __init__(self, pattern: str, *args: 'StatementInterface'):
        self._pattern = pattern
        self._replacements = args

    def append(self, pattern: str, *args: 'StatementInterface') -> 'ExpressionInterface':
        merged = [*self._replacements, *args]
        return Expression(
            '{} {}'.format(self._pattern, pattern),
            *merged
        )

    def sql(self, engine: 'EngineInterface') -> str:
        return self._pattern.format(*map(engine.extract_sql(), self._replacements))

    def params(self, engine: 'EngineInterface') -> Tuple:
        return engine.flatten_params(*self._replacements)
