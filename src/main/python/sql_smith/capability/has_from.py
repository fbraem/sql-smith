from typing import Union

from sql_smith.functions import identify_all, listing


class HasFromMixin:
    def from_(self, *tables: Union[str, 'ExpressionInterface']):
        self._from = identify_all(*tables)
        return self

    def add_from(self, *tables: Union[str, 'ExpressionInterface']):
        self._from = (*self._from, *identify_all(*tables))
        return self

    def _apply_from(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        if self._from:
            return query.append('FROM {}', listing(self._from))
        return query
