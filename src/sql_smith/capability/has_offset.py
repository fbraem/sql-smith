from sql_smith.functions import literal


class HasOffsetMixin:
    def offset(self, new_offset: int = None):
        self._offset = new_offset
        return self

    def _apply_offset(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('OFFSET {}', literal(self._offset)) if self._offset else query
