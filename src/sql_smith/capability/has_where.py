class HasWhereMixin:
    def where(self, criteria: 'CriteriaInterface'):
        self._where = criteria
        return self

    def and_where(self, criteria: 'CriteriaInterface'):
        if self._where is None:
            return self.where(criteria)

        self._where = self._where.and_(criteria)
        return self

    def or_where(self, criteria: 'CriteriaInterface'):
        if self._where is None:
            return self.where(criteria)

        self._where = self._where.or_(criteria)
        return self

    def _apply_where(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('WHERE {}', self._where) if self._where else query
