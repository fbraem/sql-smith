from sql_smith.functions import identify


class HasReturningMixin:
    def returning(self, column: str):
        self._returning = identify(column)
        return self

    def _apply_returning(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('RETURNING {}', self._returning) if self._returning else query
