from abc import abstractmethod
from typing import Callable, Tuple


class EngineInterface:
    @abstractmethod
    def make_select(self) -> 'SelectQuery':
        raise NotImplementedError('Must override make_select')

    @abstractmethod
    def make_insert(self) -> 'InsertQuery':
        raise NotImplementedError('Must override make_insert')

    @abstractmethod
    def make_update(self) -> 'UpdateQuery':
        raise NotImplementedError('Must override make_update')
    
    @abstractmethod
    def make_delete(self) -> 'DeleteQuery':
        raise NotImplementedError('Must override make_delete')

    @abstractmethod
    def escape_identifier(self, identifier: str) -> str:
        raise NotImplementedError('Must override escape_identifier')

    @abstractmethod
    def escape_like(self, parameter: str) -> str:
        raise NotImplementedError('Must override escape_like')

    @abstractmethod
    def extract_params(self) -> Callable:
        raise NotImplementedError('Must override extract_params')

    @abstractmethod
    def extract_sql(self) -> Callable:
        raise NotImplementedError('Must override extract_sql')

    @abstractmethod
    def flatten_params(self, *args: 'StatementInterface') -> Tuple:
        raise NotImplementedError('Must override flatten_params')

    @abstractmethod
    def flatten_sql(self, separator: str, *args: 'StatementInterface') -> str:
        raise NotImplementedError('Must override flatten_sql')

    @abstractmethod
    def export_parameter(self, param) -> str:
        raise NotImplementedError('Must override export_parameter')

    @abstractmethod
    def get_parameter_placeholder(self) -> str:
        raise NotImplementedError('Must override get_parameter')
