from typing import Tuple

from sql_smith.interfaces import CriteriaInterface


class Criteria(CriteriaInterface):
    def __init__(self, expression: 'ExpressionInterface'):
        self._expression = expression

    def and_(self, right: 'CriteriaInterface') -> 'CriteriaInterface':
        return Criteria(self._expression.append('AND {}', right))

    def or_(self, right: 'CriteriaInterface') -> 'CriteriaInterface':
        return Criteria(self._expression.append('OR {}', right))

    def sql(self, engine: 'EngineInterface') -> str:
        return self._expression.sql(engine)

    def params(self, engine: 'EngineInterface') -> Tuple:
        return self._expression.params(engine)
