import unittest
from typing import Tuple

from sql_smith.engine import BasicEngine
from sql_smith.query_factory import QueryFactory
from sql_smith.interfaces.query_interface import QueryInterface


class SqlTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._engine = None
        self._factory = None

    def setUp(self) -> None:
        self._engine = self.get_engine()
        self._factory = QueryFactory(self._engine)

    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return BasicEngine()

    def assertSql(self, sql: str, statement: 'StatementInterface') -> None:
        self.assertEqual(sql, statement.sql(self._engine))
        if not isinstance(statement, QueryInterface):
            return

        self.assertEqual(sql, statement.compile().sql)

    def assertParams(self, params: Tuple, statement: 'StatementInterface') -> None:
        self.assertEqual(params, statement.params(self._engine))
        if not isinstance(statement, QueryInterface):
            return

        self.assertEqual(params, statement.compile().params)
