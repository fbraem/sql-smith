from sql_smith.functions import order, listing


class HasOrderByMixin:
    def order_by(self, column: str | None = None, direction: str | None = None):
        if column:
            self._order_by.append(order(column, direction))
            return self

        self._order_by = []
        return self

    @property
    def has_order(self) -> bool:
        return len(self._order_by) > 0

    def _apply_order_by(self, query: "ExpressionInterface") -> "ExpressionInterface":
        return (
            query.append("ORDER BY {}", listing(self._order_by))
            if len(self._order_by) > 0
            else query
        )
