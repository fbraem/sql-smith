import unittest

from sql_smith.engine import SqlServerEngine
from sql_test_case import SqlTestCase


class SqlServerDeleteTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return SqlServerEngine()

    def test_limit(self) -> None:
        select = self._factory \
            .delete('users') \
            .limit(10)

        self.assertSql('DELETE TOP(10) FROM [users]', select)
        self.assertParams((), select)


if __name__ == '__main__':
    unittest.main()
