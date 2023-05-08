from dataclasses import dataclass

from sql_smith.interfaces import ExpressionInterface


class HasCteMixin:
    def with_(self, name: str | None = None, query: ExpressionInterface | None = None):
        if name is None:
            self._cte = {}
        else:
            self._cte[name] = query
        return self

    def _apply_with(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        if len(self._cte) > 0:
            for name, cte_query in self._cte.items():
                query = query.append(name + ' AS ({})', cte_query)
        return query
