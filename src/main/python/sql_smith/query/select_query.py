from sql_smith.capability \
    import HasFromMixin, HasWhereMixin, HasLimitMixin, HasOffsetMixin, HasOrderByMixin, CanUnionMixin
from sql_smith.functions import identify_all, express, listing, identify
from .abstract_query import AbstractQuery


class SelectQuery(
    CanUnionMixin, HasFromMixin, HasOrderByMixin, HasWhereMixin, HasLimitMixin, HasOffsetMixin, AbstractQuery
):
    """Implements a SELECT query."""
    def __init__(self, engine: 'EngineInterface'):
        super().__init__(engine)
        self._from = ()
        self._limit = None
        self._offset = None
        self._order_by = []
        self._where = None

        self._distinct = False
        self._columns = []
        self._joins = []
        self._group_by = []
        self._having = None

    def distinct(self, state: bool = True) -> 'SelectQuery':
        """Add or remove DISTINCT."""
        self._distinct = state
        return self

    def columns(self, *columns) -> 'SelectQuery':
        """Set the columns to select."""
        self._columns = identify_all(*columns)
        return self

    def add_columns(self, *columns):
        """Add columns to the selection."""
        self._columns = (*self._columns, *identify_all(*columns))
        return self

    def join(self, table: str, criteria: 'CriteriaInterface', join_type: str = '') -> 'SelectQuery':
        """Add a join."""
        sql = '{} JOIN {{}} ON {{}}'.format(join_type.upper()).strip()
        self._joins.append(express(sql, identify(table), criteria))
        return self

    def inner_join(self, table: str, criteria: 'CriteriaInterface') -> 'SelectQuery':
        """Add an INNER join."""
        return self.join(table, criteria, 'INNER')

    def left_join(self, table: str, criteria: 'CriteriaInterface') -> 'SelectQuery':
        """Add a LEFT join."""
        return self.join(table, criteria, 'LEFT')

    def right_join(self, table: str, criteria: 'CriteriaInterface') -> 'SelectQuery':
        """Add a RIGHT join."""
        return self.join(table, criteria, 'RIGHT')

    def full_join(self, table: str, criteria: 'CriteriaInterface') -> 'SelectQuery':
        """Add a FULL join."""
        return self.join(table, criteria, 'FULL')

    def group_by(self, *columns):
        """Add a GROUP BY clause."""
        self._group_by = identify_all(*columns)
        return self

    def having(self, criteria: 'CriteriaInterface'):
        """Add an HAVING clause."""
        self._having = criteria
        return self

    def as_expression(self) -> 'ExpressionInterface':
        query = self.start_expression()
        query = self.__apply_distinct(query)
        query = self.__apply_columns(query)
        query = self._apply_from(query)
        query = self.__apply_joins(query)
        query = self._apply_where(query)
        query = self.__apply_group_by(query)
        query = self.__apply_having(query)
        query = self._apply_order_by(query)
        query = self._apply_limit(query)
        query = self._apply_offset(query)
        return query

    def start_expression(self) -> 'ExpressionInterface':
        return express('SELECT')

    def __apply_columns(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        if len(self._columns) > 0:
            return query.append('{}', listing(self._columns))
        return query.append('*')

    def __apply_distinct(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        if self._distinct:
            return query.append('DISTINCT')
        return query

    def __apply_joins(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('{}', listing(self._joins, ' ')) if len(self._joins) > 0 else query

    def __apply_group_by(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('GROUP BY {}', listing(self._group_by, ' ')) if len(self._group_by) > 0 else query

    def __apply_having(self, query: 'ExpressionInterface') -> 'ExpressionInterface':
        return query.append('HAVING {}', self._having) if self._having else query
