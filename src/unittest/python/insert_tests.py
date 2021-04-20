import unittest

from sql_test_case import SqlTestCase


class InsertTests(SqlTestCase):
    def test_insert(self) -> None:
        insert = self._factory.insert('users')

        self.assertSql('INSERT INTO users', insert)
        self.assertParams((), insert)

    def test_map(self) -> None:
        insert = self._factory \
            .insert(
                'users',
                {
                    'id': 1,
                    'username': 'admin'
                }
            )

        self.assertSql('INSERT INTO users (id, username) VALUES (?, ?)', insert)
        self.assertParams((1, 'admin'), insert)

    def test_multiple(self) -> None:
        insert = self._factory \
            .insert('users') \
            .columns('id', 'username') \
            .values(2, 'jenny') \
            .values(3, 'rick')

        self.assertSql('INSERT INTO users (id, username) VALUES (?, ?), (?, ?)', insert)
        self.assertParams((2, 'jenny', 3, 'rick'), insert)


if __name__ == '__main__':
    unittest.main()
