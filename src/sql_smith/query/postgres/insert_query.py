from sql_smith.capability import HasReturningMixin
from sql_smith.query import InsertQuery as BaseInsertQuery


class InsertQuery(HasReturningMixin, BaseInsertQuery):
    """Postgres InsertQuery that supports RETURNING."""
    def as_expression(self) -> 'ExpressionInterface':
        query = super().as_expression()
        query = self._apply_returning(query)
        return query
