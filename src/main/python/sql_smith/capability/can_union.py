class CanUnionMixin:
    def union(self, right: 'StatementInterface') -> 'UnionQuery':
        from sql_smith.query.union_query import UnionQuery
        return UnionQuery(self._engine, self, right)

    def union_all(self, right: 'StatementInterface') -> 'UnionQuery':
        return self.union(right).all()
