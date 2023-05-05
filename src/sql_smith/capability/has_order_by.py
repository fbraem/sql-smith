from sql_smith.functions import order, listing


class HasOrderByMixin:
    def order_by(self, column: str = None, direction: str = None):
        if column:
            self._order_by.append(order(column, direction))
            return self

        self._order_by = []
        return self

    def _apply_order_by(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('ORDER BY {}', listing(self._order_by)) if len(self._order_by) > 0 else query
