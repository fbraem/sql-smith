from sql_smith.functions import literal
from sql_smith.query import DeleteQuery as BaseDeleteQuery


class DeleteQuery(BaseDeleteQuery):
    """Sql Server DeleteQuery to support LIMIT."""
    def start_expression(self) -> 'ExpressionInterface':
        query = super().start_expression()
        if self._limit is None:
            return query
        return query.append('TOP({})', literal(self._limit))

    def _apply_limit(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query
