from sql_smith.capability import HasReturningMixin
from sql_smith.query import UpdateQuery as BaseUpdateQuery


class UpdateQuery(HasReturningMixin, BaseUpdateQuery):
    def as_expression(self) -> 'ExpressionInterface':
        query = super().as_expression()
        query = self._apply_returning(query)
        return query
