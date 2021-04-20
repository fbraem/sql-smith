from sql_smith.functions import criteria
from sql_smith.partial import LikeBegins, LikeContains, LikeEnds


class LikeBuilder:
    def __init__(self, statement: 'StatementInterface'):
        self._statement = statement

    def begins(self, value: str) -> 'CriteriaInterface':
        return self.__like(LikeBegins(value))

    def not_begins(self, value: str) -> 'CriteriaInterface':
        return self.__not_like(LikeBegins(value))

    def contains(self, value: str) -> 'CriteriaInterface':
        return self.__like(LikeContains(value))

    def not_contains(self, value: str) -> 'CriteriaInterface':
        return self.__not_like(LikeContains(value))

    def ends(self, value: str) -> 'CriteriaInterface':
        return self.__like(LikeEnds(value))

    def not_ends(self, value: str) -> 'CriteriaInterface':
        return self.__not_like(LikeEnds(value))

    def __like(self, value: 'StatementInterface') -> 'CriteriaInterface':
        return criteria('{} LIKE {}', self._statement, value)

    def __not_like(self, value: 'StatementInterface') -> 'CriteriaInterface':
        return criteria('{} NOT LIKE {}', self._statement, value)
