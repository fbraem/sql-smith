from abc import abstractmethod

from .statement_interface import StatementInterface


class ExpressionInterface(StatementInterface):
    @abstractmethod
    def append(self, pattern: str, *replacements: 'StatementInterface') -> 'ExpressionInterface':
        raise NotImplementedError('append must be implemented')
