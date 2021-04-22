from sql_smith.capability import CanUnionMixin, HasOrderByMixin
from sql_smith.functions import express
from sql_smith.query import AbstractQuery


class UnionQuery(CanUnionMixin, HasOrderByMixin, AbstractQuery):
    """Implements a union query."""
    def __init__(self, engine: 'EngineInterface', left: 'StatementInterface', right: 'StatementInterface'):
        super().__init__(engine)
        self._order_by = []
        self._all = False
        self._left = left
        self._right = right

    def all(self, state: bool = True) -> 'UnionQuery':
        """Sets ALL."""
        self._all = state
        return self

    def as_expression(self) -> 'ExpressionInterface':
        query = self.start_expression()
        query = self.__apply_all(query)
        query = self.__apply_right(query)
        query = self._apply_order_by(query)
        return query

    def start_expression(self) -> 'ExpressionInterface':
        return express('{} UNION', self._left)

    def __apply_all(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('ALL') if self._all else query

    def __apply_right(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('{}', self._right)
