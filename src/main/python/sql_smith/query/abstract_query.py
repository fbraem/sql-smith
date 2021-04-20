from abc import abstractmethod

from sql_smith.interfaces import QueryInterface, EngineInterface
from sql_smith.query.query import Query


class AbstractQuery(QueryInterface):
    def __init__(self, engine: 'EngineInterface'):
        super().__init__()
        self._engine = engine

    @abstractmethod
    def as_expression(self) -> 'ExpressionInterface':
        raise NotImplementedError('Must override as_expression')

    @abstractmethod
    def start_expression(self) -> 'ExpressionInterface':
        raise NotImplementedError('Must override start_expression')

    def compile(self) -> 'Query':
        query = self.as_expression()
        return Query(
            query.sql(self._engine),
            query.params(self._engine)
        )

    def sql(self, engine: 'EngineInterface') -> str:
        return self.as_expression().sql(engine)

    def params(self, engine: 'EngineInterface') -> str:
        return self.as_expression().params(engine)
