import unittest

from sql_test_case import SqlTestCase


class InsertTests(SqlTestCase):
    def test_insert(self) -> None:
        insert = self._factory.insert('users')

        self.assertSql('INSERT INTO users', insert)
        self.assertParams((), insert)

    def test_map(self) -> None:
        new_row = {
            'id': 1,
            'username': 'admin'
        }

        insert = self._factory \
            .insert('users', new_row)

        # Before python 3.7, dict is not ordered by insertion.
        # So, check it dynamically to make this test work in 3.5 and 3.6
        columns = ', '.join(new_row.keys())
        values = tuple(new_row.values())
        self.assertSql('INSERT INTO users ({}) VALUES (?, ?)'.format(columns), insert)
        self.assertParams(values, insert)

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
