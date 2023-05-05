from abc import abstractmethod
from typing import Tuple


class StatementInterface:
    @abstractmethod
    def sql(self, engine: 'EngineInterface') -> str:
        raise NotImplementedError('sql must be implemented')

    @abstractmethod
    def params(self, engine: 'EngineInterface') -> Tuple:
        raise NotImplementedError('params must be implemented')
