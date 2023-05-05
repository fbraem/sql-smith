from sql_smith.functions import literal
from sql_smith.query import SelectQuery as BaseSelectQuery


class SelectQuery(BaseSelectQuery):
    """Sql Server SelectQuery to support offset and limit."""
    def _apply_offset(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        if self._offset is None or self._limit is None:
            return query
        return query.append('OFFSET {} ROWS FETCH NEXT {} ROWS ONLY', literal(self._offset), literal(self._limit))

    def _apply_limit(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query
