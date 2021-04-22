from sql_smith.query import SelectQuery as BaseSelectQuery


class SelectQuery(BaseSelectQuery):
    """Mysql SelectQuery that supports SQL_CALC_FOUND_ROWS."""
    def __init__(self, engine: 'EngineInterface'):
        super().__init__(engine)
        self._calc_found_rows = False

    def calc_found_rows(self, status: bool) -> 'MySqlSelectQuery':
        self._calc_found_rows = status
        return self

    def start_expression(self) -> 'ExpressionInterface':
        query = super().start_expression()
        if self._calc_found_rows:
            query = query.append('SQL_CALC_FOUND_ROWS')
        return query
