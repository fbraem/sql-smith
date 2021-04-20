from typing import Union, Dict, Any

from sql_smith.engine import BasicEngine


class QueryFactory:
    def __init__(self, engine: 'EngineInterface' = None):
        if engine is None:
            self._engine = BasicEngine()
        else:
            self._engine = engine

    def select(self, *columns: Union[str, 'StatementInterface']) -> 'SelectQuery':
        query = self._engine.make_select()
        if len(columns) == 0:
            return query

        return query.columns(*columns)

    def select_distinct(self, *columns: Union[str, 'StatementInterface']) -> 'SelectQuery':
        return self.select(*columns).distinct()

    def insert(self, table: str, column_values: Dict[str, Any] = None) -> 'InsertQuery':
        query = self._engine.make_insert().into(table)
        if column_values:
            query = query.map(column_values)

        return query

    def delete(self, table: str) -> 'DeleteQuery':
        return self._engine.make_delete().from_(table)

    def update(self, table: str, value_set=None) -> 'UpdateQuery':
        query = self._engine.make_update().table(table)
        if value_set:
            query.set(value_set)

        return query
