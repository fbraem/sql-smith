import unittest

from sql_smith.functions import alias, on, field, func, express, identify
from sql_test_case import SqlTestCase


class SelectTests(SqlTestCase):
    def test_select(self) -> None:
        select = self._factory.select().from_('users')
        self.assertSql('SELECT * FROM users', select)
        self.assertParams((), select)

    def test_distinct(self) -> None:
        select = self._factory.select().distinct()
        self.assertSql('SELECT DISTINCT *', select)
        self.assertParams((), select)

    def test_columns(self) -> None:
        select = self._factory \
            .select('id', 'username') \
            .from_('users')
        self.assertSql('SELECT id, username FROM users', select)
        self.assertParams((), select)

    def test_join(self) -> None:
        select = self._factory \
            .select('u.username', 'r.role', 'c.country') \
            .from_(alias('users', 'u')) \
            .join(alias('roles', 'r'), on('u.role_id', 'r.id')) \
            .join(alias('countries', 'c'), on('u.country_id', 'c.id'))
        self.assertSql(
            ' '.join([
                'SELECT u.username, r.role, c.country',
                'FROM users AS u',
                'JOIN roles AS r ON u.role_id = r.id',
                'JOIN countries AS c ON u.country_id = c.id'
            ]),
            select
        )
        self.assertParams((), select)

    def test_join_inner(self) -> None:
        select = self._factory \
            .select('u.username', 'c.country') \
            .from_(alias('users', 'u')) \
            .inner_join(alias('countries', 'c'), on('u.country_id', 'c.id'))

        self.assertSql(
            ' '.join([
                'SELECT u.username, c.country',
                'FROM users AS u',
                'INNER JOIN countries AS c ON u.country_id = c.id',
            ]),
            select
        )
        self.assertParams((), select)

    def test_join_left(self) -> None:
        select = self._factory \
            .select('u.username', 'c.country') \
            .from_(alias('users', 'u')) \
            .left_join(alias('countries', 'c'), on('u.country_id', 'c.id'))

        self.assertSql(
            ' '.join([
                'SELECT u.username, c.country',
                'FROM users AS u',
                'LEFT JOIN countries AS c ON u.country_id = c.id',
            ]),
            select
        )
        self.assertParams((), select)

    def test_join_right(self) -> None:
        select = self._factory \
            .select('u.username', 'c.country') \
            .from_(alias('users', 'u')) \
            .right_join(alias('countries', 'c'), on('u.country_id', 'c.id'))

        self.assertSql(
            ' '.join([
                'SELECT u.username, c.country',
                'FROM users AS u',
                'RIGHT JOIN countries AS c ON u.country_id = c.id',
            ]),
            select
        )
        self.assertParams((), select)

    def test_join_full(self) -> None:
        select = self._factory \
            .select('u.username', 'c.country') \
            .from_(alias('users', 'u')) \
            .full_join(alias('countries', 'c'), on('u.country_id', 'c.id'))

        self.assertSql(
            ' '.join([
                'SELECT u.username, c.country',
                'FROM users AS u',
                'FULL JOIN countries AS c ON u.country_id = c.id',
            ]),
            select
        )
        self.assertParams((), select)

    def test_where(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .where(field('id').eq(1))

        self.assertSql('SELECT * FROM users WHERE id = ?', select)
        self.assertParams((1,), select)

    def test_where_and(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .and_where(field('id').eq(1)) \
            .and_where(field('username').eq('admin'))

        self.assertSql('SELECT * FROM users WHERE id = ? AND username = ?', select)
        self.assertParams((1, 'admin'), select)

    def test_group_by(self) -> None:
        select = self._factory \
            .select(
                alias(func('COUNT', 'id'), 'total')
            ) \
            .from_('employees') \
            .group_by('department')

        self.assertSql(
            ' '.join([
                'SELECT COUNT(id) AS total',
                'FROM employees',
                'GROUP BY department'
            ]),
            select
        )
        self.assertParams((), select)

    def test_having(self) -> None:
        salary_sum = func('SUM', 'salary')
        select = self._factory \
            .select(
                'department',
                alias(salary_sum, 'total')
            ) \
            .from_('employees') \
            .group_by('department') \
            .having(field(salary_sum).gt(5000))

        self.assertSql(
            ' '.join([
                'SELECT department, SUM(salary) AS total',
                'FROM employees',
                'GROUP BY department',
                'HAVING SUM(salary) > ?'
            ]),
            select
        )
        self.assertParams((5000, ), select)

    def test_order_by(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .order_by('birthday')

        self.assertSql('SELECT * FROM users ORDER BY birthday', select)
        self.assertParams((), select)

    def test_order_by_direction(self) -> None:
        select = self._factory \
            .select(
                'u.id',
                'u.username',
                alias(func('COUNT', 'l.id'), 'total')
            ) \
            .from_(alias('users', 'u')) \
            .join(alias('logins', 'l'), on('u.id', 'l.user_id')) \
            .group_by('l.user_id') \
            .order_by('u.username') \
            .order_by('total', 'desc')

        self.assertSql(
            ' '.join([
                'SELECT u.id, u.username, COUNT(l.id) AS total',
                'FROM users AS u',
                'JOIN logins AS l ON u.id = l.user_id',
                'GROUP BY l.user_id',
                'ORDER BY u.username, total DESC',
            ]),
            select
        )
        self.assertParams((), select)

    def test_order_by_reset(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .order_by('birthday')

        select.order_by()

        self.assertSql('SELECT * FROM users', select)
        self.assertParams((), select)

    def test_order_by_expr(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .order_by(express("FIELD({}, 'off')", identify('status')), 'DESC')

        self.assertSql("SELECT * FROM users ORDER BY FIELD(status, 'off') DESC", select)
        self.assertParams((), select)

    def test_offset_limit(self) -> None:
        select = self._factory \
            .select() \
            .from_('users') \
            .limit(10) \
            .offset(100)

        self.assertSql('SELECT * FROM users LIMIT 10 OFFSET 100', select)
        self.assertParams((), select)

    def test_union(self) -> None:
        a = self._factory.select('supplier_id').from_('suppliers')
        b = self._factory.select('supplier_id').from_('orders')

        union = a.union(b).order_by('supplier_id', 'desc')

        self.assertSql(
            ' '.join([
                'SELECT supplier_id FROM suppliers',
                'UNION',
                'SELECT supplier_id FROM orders',
                'ORDER BY supplier_id DESC'
            ]),
            union
        )
        self.assertParams((), union)

    def test_union_all(self) -> None:
        a = self._factory.select('first_name', 'last_name').from_('employees')
        b = self._factory.select('first_name', 'last_name').from_('customers')
        c = self._factory.select('first_name', 'last_name').from_('partners')

        union = a.union_all(b).union_all(c)

        self.assertSql(
            ' '.join([
                'SELECT first_name, last_name FROM employees',
                'UNION ALL',
                'SELECT first_name, last_name FROM customers',
                'UNION ALL',
                'SELECT first_name, last_name FROM partners'
            ]),
            union
        )
        self.assertParams((), union)


if __name__ == '__main__':
    unittest.main()
