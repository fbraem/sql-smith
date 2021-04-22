from typing import Dict, Any, Union

from sql_smith.capability import HasWhereMixin
from sql_smith.functions import identify, param, express, listing
from sql_smith.query import AbstractQuery


class UpdateQuery(HasWhereMixin, AbstractQuery):
    """Implements an UPDATE query."""
    def __init__(self, engine: 'EngineInterface'):
        super().__init__(engine)
        self._table = None
        self._set = None
        self._where = []

    def table(self, table: Union[str, 'StatementInterface']) -> 'UpdateQuery':
        """Sets the table."""
        self._table = identify(table)
        return self

    def set(self, value_dict: Dict[str, Any]):
        """Sets the column and values with a dictionary."""
        self._set = listing(list(map(
            lambda k, v: express('{} = {}', identify(k), param(v)),
            value_dict.keys(),
            value_dict.values()
        )))
        return self

    def as_expression(self) -> 'ExpressionInterface':
        query = self.start_expression()
        query = self.__apply_table(query)
        query = self.__apply_set(query)
        query = self._apply_where(query)

        return query

    def start_expression(self) -> 'ExpressionInterface':
        return express('UPDATE')

    def __apply_table(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('{}', self._table) if self._table else query

    def __apply_set(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('SET {}', self._set) if self._set else query
