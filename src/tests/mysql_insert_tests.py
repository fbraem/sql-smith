import unittest

from sql_smith.engine.mysql_engine import MysqlEngine
from .sql_test_case import SqlTestCase


class MySqlInsertTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> "EngineInterface":
        return MysqlEngine()

    def test_calc_found_rows(self) -> None:
        insert = self._factory.insert("users", {"username": "james"}).ignore(True)

        self.assertSql("INSERT IGNORE INTO `users` (`username`) VALUES (%s)", insert)
        self.assertParams(("james",), insert)


if __name__ == "__main__":
    unittest.main()
