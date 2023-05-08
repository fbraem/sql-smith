import unittest

from sql_smith.engine.mysql_engine import MysqlEngine
from sql_smith.functions import identify, field
from .sql_test_case import SqlTestCase


class MysqlEngineTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> "EngineInterface":
        return MysqlEngine()

    def test_identifier(self) -> None:
        f = identify("id")
        self.assertSql("`id`", f)

    def test_bool_parameter_value(self) -> None:
        criteria = field("active").eq(True)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual("`active` = true", sql)
        self.assertEqual((), params)

        criteria = field("active").eq(False)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual("`active` = false", sql)
        self.assertEqual((), params)

        criteria = field("active").eq(None)
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual("`active` = NULL", sql)
        self.assertEqual((), params)

        criteria = field("active").eq("yes")
        sql = criteria.sql(self._engine)
        params = criteria.params(self._engine)
        self.assertEqual("`active` = %s", sql)
        self.assertEqual(("yes",), params)


if __name__ == "__main__":
    unittest.main()
