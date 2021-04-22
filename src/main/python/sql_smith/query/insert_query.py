from typing import Dict, Any

from sql_smith.functions import express, identify, listing, identify_all, param_all
from sql_smith.query import AbstractQuery


class InsertQuery(AbstractQuery):
    """Implements the INSERT query."""
    def __init__(self, engine: 'EngineInterface'):
        AbstractQuery.__init__(self, engine)
        self._into = None
        self._columns = None
        self._values = []

    def into(self, table: str) -> 'InsertQuery':
        """Sets the table."""
        self._into = identify(table)
        return self

    def map(self, column_values: Dict[str, Any]):
        """Maps a dictionary to columns and values."""
        return self.columns(*column_values.keys()).values(*column_values.values())

    def columns(self, *columns) -> 'InsertQuery':
        """Sets the columns to insert."""
        self._columns = listing(identify_all(*columns))
        return self

    def values(self, *values) -> 'InsertQuery':
        """Appends values."""
        self._values.append(express('({})', listing(param_all(*values))))
        return self

    def as_expression(self) -> 'ExpressionInterface':
        query = self.start_expression()
        query = self.__apply_into(query)
        query = self.__apply_columns(query)
        query = self.__apply_values(query)

        return query

    def start_expression(self) -> 'ExpressionInterface':
        return express('INSERT')

    def __apply_into(self, query):
        return query.append('INTO {}', self._into) if self._into else query

    def __apply_columns(self, query):
        return query.append('({})', self._columns) if self._columns else query

    def __apply_values(self, query):
        return query.append('VALUES {}', listing(self._values)) if self._values else query
