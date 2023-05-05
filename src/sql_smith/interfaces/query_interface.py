from abc import abstractmethod

from .statement_interface import StatementInterface


class QueryInterface(StatementInterface):
    @abstractmethod
    def as_expression(self) -> 'ExpressionInterface':
        raise NotImplementedError('as_expression must be implemented')

    @abstractmethod
    def compile(self) -> 'Query':
        raise NotImplementedError('compile must be implemented')
