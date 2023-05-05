from sql_smith.functions import criteria, listing


class CriteriaBuilder:
    def __init__(self, statement: 'StatementInterface'):
        self._statement = statement

    def between(self, start, end) -> 'CriteriaInterface':
        return criteria('{} BETWEEN {} AND {}', self._statement, start, end)

    def not_between(self, start, end) -> 'CriteriaInterface':
        return criteria('{} NOT BETWEEN {} AND {}', self._statement, start, end)

    def in_(self, *args) -> 'CriteriaInterface':
        return criteria('{} IN ({})', self._statement, listing(args))

    def not_in(self, *args) -> 'CriteriaInterface':
        return criteria('{} NOT IN ({})', self._statement, listing(args))

    def eq(self, value) -> 'CriteriaInterface':
        return criteria('{} = {}', self._statement, value)

    def not_eq(self, value) -> 'CriteriaInterface':
        return criteria('{} != {}', self._statement, value)

    def gt(self, value) -> 'CriteriaInterface':
        return criteria('{} > {}', self._statement, value)

    def gte(self, value) -> 'CriteriaInterface':
        return criteria('{} >= {}', self._statement, value)

    def lt(self, value) -> 'CriteriaInterface':
        return criteria('{} < {}', self._statement, value)

    def lte(self, value) -> 'CriteriaInterface':
        return criteria('{} <= {}', self._statement, value)

    def is_null(self) -> 'CriteriaInterface':
        return criteria('{} IS NULL', self._statement)

    def is_not_null(self) -> 'CriteriaInterface':
        return criteria('{} IS NOT NULL', self._statement)
