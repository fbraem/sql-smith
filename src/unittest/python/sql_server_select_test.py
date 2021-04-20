import unittest

from sql_smith.engine import SqlServerEngine
from sql_test_case import SqlTestCase


class SqlServerSelectTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return SqlServerEngine()

    def test_limit_without_offset(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .limit(10)

        self.assertSql('SELECT * FROM [users]', select)
        self.assertParams((), select)

    def test_limit_without_limit(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .offset(10)

        self.assertSql('SELECT * FROM [users]', select)
        self.assertParams((), select)

    def test_offset_limit(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .order_by('id') \
            .offset(0) \
            .limit(10)

        self.assertSql(
            ' '.join([
                'SELECT *',
                'FROM [users]',
                'ORDER BY [id]',
                'OFFSET 0 ROWS',
                'FETCH NEXT 10 ROWS ONLY'
            ]),
            select
        )
        self.assertParams((), select)


if __name__ == '__main__':
    unittest.main()
