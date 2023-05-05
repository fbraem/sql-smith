from sql_smith.functions import literal


class HasLimitMixin:
    def limit(self, new_limit: int = None):
        self._limit = new_limit
        return self

    def _apply_limit(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('LIMIT {}', literal(self._limit)) if self._limit else query
