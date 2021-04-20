import unittest

from sql_smith.functions import field
from sql_test_case import SqlTestCase


class UpdateTests(SqlTestCase):
    def test_update(self) -> None:
        update = self._factory.update('users')

        self.assertSql('UPDATE users', update)
        self.assertParams((), update)

    def test_set(self) -> None:
        update = self._factory.update('users', {'last_login': None})

        self.assertSql('UPDATE users SET last_login = NULL', update)
        self.assertParams((), update)

    def test_where(self) -> None:
        update = self._factory \
            .update(
                'users', {
                    'username': 'wonder_woman'
                }
            )\
            .where(field('id').eq(50))

        self.assertSql('UPDATE users SET username = ? WHERE id = ?', update)
        self.assertParams(('wonder_woman', 50), update)


if __name__ == '__main__':
    unittest.main()
