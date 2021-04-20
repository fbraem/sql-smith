from abc import abstractmethod

from .statement_interface import StatementInterface


class CriteriaInterface(StatementInterface):
    @abstractmethod
    def and_(self, right: 'CriteriaInterface') -> 'CriteriaInterface':
        raise NotImplementedError('and_ must be implemented')

    @abstractmethod
    def or_(self, right: 'CriteriaInterface') -> 'CriteriaInterface':
        raise NotImplementedError('or_ must be implemented')
