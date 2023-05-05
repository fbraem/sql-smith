import unittest

from sql_smith.engine.sqlite_engine import SqliteEngine
from sql_smith.functions import identify, field
from .sql_test_case import SqlTestCase


class SqliteEngineTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return SqliteEngine()

    def test_identifier(self) -> None:
        f = identify('id')
        self.assertSql('id', f)

    def test_bool_parameter_value(self) -> None:
        criteria = field('active').eq(True)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual('active = 1', sql)
        self.assertEqual((), params)

        criteria = field('active').eq(False)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual('active = 0', sql)
        self.assertEqual((), params)

        criteria = field('active').eq(None)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual('active = NULL', sql)
        self.assertEqual((), params)

        criteria = field('active').eq('yes')
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual('active = ?', sql)
        self.assertEqual(('yes', ), params)


if __name__ == '__main__':
    unittest.main()
