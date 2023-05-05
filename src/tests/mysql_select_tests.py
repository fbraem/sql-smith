import unittest

from sql_smith.engine.mysql_engine import MysqlEngine
from .sql_test_case import SqlTestCase


class MySqlSelectTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return MysqlEngine()

    def test_calc_found_rows(self) -> None:
        select = self._factory \
            .select() \
            .calc_found_rows(True) \
            .from_('users') \
            .limit(10)

        self.assertSql('SELECT SQL_CALC_FOUND_ROWS * FROM `users` LIMIT 10', select)
        self.assertParams((), select)

    def test_select_qualified_start(self) -> None:
        query = self._factory \
            .select('a.*', 'b.id', 'b.name') \
            .from_('tests')
        self.assertSql('SELECT `a`.*, `b`.`id`, `b`.`name` FROM `tests`', query)


if __name__ == '__main__':
    unittest.main()
