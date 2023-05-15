from sql_smith.functions import literal


class HasOffsetMixin:
    def offset(self, new_offset: int | None = None):
        self._offset = new_offset
        return self

    @property
    def has_offset(self):
        """Return True when the query has an offset."""
        return self._offset is not None

    def _apply_offset(self, query: "ExpressionInterface") -> "ExpressionInterface":
        return (
            query.append("OFFSET {}", literal(self._offset)) if self._offset else query
        )
