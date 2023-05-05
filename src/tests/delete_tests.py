import unittest

from sql_smith.functions import field
from .sql_test_case import SqlTestCase


class DeleteTests(SqlTestCase):
    def test_update(self) -> None:
        delete = self._factory.delete('users')

        self.assertSql('DELETE FROM users', delete)
        self.assertParams((), delete)

    def test_where(self) -> None:
        delete = self._factory \
            .delete('users') \
            .where(field('id').eq(5))

        self.assertSql('DELETE FROM users WHERE id = ?', delete)
        self.assertParams((5, ), delete)


if __name__ == '__main__':
    unittest.main()
