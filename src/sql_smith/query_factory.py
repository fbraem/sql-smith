from typing import Union, Dict, Any

from sql_smith.engine import BasicEngine


class QueryFactory:
    """Factory class for creating queries
    """
    def __init__(self, engine: 'EngineInterface' = None):
        if engine is None:
            self._engine = BasicEngine()
        else:
            self._engine = engine

    def select(self, *columns: Union[str, 'StatementInterface']) -> 'SelectQuery':
        """Create a SELECT query
        """
        query = self._engine.make_select()
        if len(columns) == 0:
            return query

        return query.columns(*columns)

    def select_distinct(self, *columns: Union[str, 'StatementInterface']) -> 'SelectQuery':
        """Create a SELECT DISTINCT query
        """
        return self.select(*columns).distinct()

    def insert(self, table: str, column_values: Dict[str, Any] = None) -> 'InsertQuery':
        """Create an INSERT query
        """
        query = self._engine.make_insert().into(table)
        if column_values:
            query = query.map(column_values)

        return query

    def delete(self, table: str) -> 'DeleteQuery':
        """Create a DELETE query
        """
        return self._engine.make_delete().from_(table)

    def update(self, table: str, value_set=None) -> 'UpdateQuery':
        """Create an UPDATE query
        """
        query = self._engine.make_update().table(table)
        if value_set:
            query.set(value_set)

        return query
