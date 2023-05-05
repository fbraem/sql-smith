import unittest

from sql_smith.engine.sql_server_engine import SqlServerEngine
from sql_smith.functions import identify, search
from .sql_test_case import SqlTestCase


class SqlServerEngineTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return SqlServerEngine()

    def test_identifier(self) -> None:
        f = identify('id')
        self.assertSql('[id]', f)

    def test_like(self) -> None:
        expr = search('username').contains('[a-z]')
        self.assertParams((r'%\[a-z\]%', ), expr)


if __name__ == '__main__':
    unittest.main()
