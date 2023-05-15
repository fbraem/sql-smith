from sql_smith.functions import literal


class HasLimitMixin:
    def limit(self, new_limit: int | None = None):
        self._limit = new_limit
        return self

    @property
    def is_limited(self) -> bool:
        """Returns True when the query has a LIMIT."""
        return self._limit is not None

    def _apply_limit(self, query: "ExpressionInterface") -> "ExpressionInterface":
        return query.append("LIMIT {}", literal(self._limit)) if self._limit else query
