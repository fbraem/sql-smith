from sql_smith.query import InsertQuery as BaseInsertQuery


class InsertQuery(BaseInsertQuery):
    """MySql InsertQuery that supports IGNORE."""
    def __init__(self, engine: 'EngineInterface'):
        super().__init__(engine)
        self._ignore = False

    def ignore(self, status: bool) -> 'MySqlSelectQuery':
        self._ignore = status
        return self

    def start_expression(self) -> 'ExpressionInterface':
        query = super().start_expression()
        if self._ignore:
            query = query.append('IGNORE')
        return query
