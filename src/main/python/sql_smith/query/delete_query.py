from sql_smith.capability import HasFromMixin, HasWhereMixin, HasLimitMixin
from sql_smith.functions import express
from sql_smith.query import AbstractQuery


class DeleteQuery(HasFromMixin, HasWhereMixin, HasLimitMixin, AbstractQuery):
    """Implements the DELETE query."""
    def __init__(self, engine: 'EngineInterface'):
        super().__init__(engine)
        self._from = ()
        self._limit = None
        self._where = None

    def as_expression(self) -> 'ExpressionInterface':
        query = self.start_expression()
        query = self._apply_from(query)
        query = self._apply_where(query)
        query = self._apply_limit(query)

        return query

    def start_expression(self) -> 'ExpressionInterface':
        return express('DELETE')
