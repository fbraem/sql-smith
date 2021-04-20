import unittest
from sql_smith.functions import field, group
from sql_test_case import SqlTestCase


class CriteriaTests(SqlTestCase):
    def test_between(self) -> None:
        expr = field('created_at').between('2018-01-01', '2018-02-01')
        self.assertSql('created_at BETWEEN ? AND ?', expr)
        self.assertParams(('2018-01-01', '2018-02-01'), expr)

        expr = field('created_at').not_between('2018-02-01', '2018-03-01')
        self.assertSql('created_at NOT BETWEEN ? AND ?', expr)
        self.assertParams(('2018-02-01', '2018-03-01'), expr)

    def test_in(self) -> None:
        expr = field('country').in_('CN', 'JP')
        self.assertSql('country IN (?, ?)', expr)
        self.assertParams(('CN', 'JP'), expr)

        expr = field('country').not_in('CA', 'US', 'MX')
        self.assertSql('country NOT IN (?, ?, ?)', expr)
        self.assertParams(('CA', 'US', 'MX'), expr)

    def test_in_query(self) -> None:
        expr = field('country').in_(
            self._factory.select_distinct('country').from_('users')
        )
        self.assertSql('country IN (SELECT DISTINCT country FROM users)', expr)
        self.assertParams((), expr)

    def test_equals(self) -> None:
        expr = field('id').eq(11)
        self.assertSql('id = ?', expr)
        self.assertParams((11,), expr)

        expr = field('id').not_eq(42)
        self.assertSql('id != ?', expr)
        self.assertParams((42,), expr)

    def test_gt(self) -> None:
        expr = field('age').gt(65)
        self.assertSql('age > ?', expr)
        self.assertParams((65,), expr)

        expr = field('age').gte(18)
        self.assertSql('age >= ?', expr)
        self.assertParams((18,), expr)

    def test_lt(self) -> None:
        expr = field('age').lt(21)
        self.assertSql('age < ?', expr)
        self.assertParams((21,), expr)

        expr = field('age').lte(30)
        self.assertSql('age <= ?', expr)
        self.assertParams((30,), expr)

    def test_null(self) -> None:
        expr = field('deleted_at').is_null()
        self.assertSql('deleted_at IS NULL', expr)
        self.assertParams((), expr)

    def test_boolean(self) -> None:
        expr = field('is_active').eq(True)
        self.assertSql('is_active = true', expr)

        expr = field('is_active').eq(False)
        self.assertSql('is_active = false', expr)

    def test_and(self) -> None:
        expr = field('id').eq(5)
        expr = expr.and_(field('is_active').eq(1))
        self.assertSql('id = ? AND is_active = ?', expr)
        self.assertParams((5, 1), expr)

    def test_or(self) -> None:
        expr = field('is_deleted').eq(1)
        expr = expr.or_(field('is_in_active').eq(1))
        self.assertSql('is_deleted = ? OR is_in_active = ?', expr)
        self.assertParams((1, 1), expr)

    def test_group(self) -> None:
        expr = group(
            field('username').eq('jane')
            .or_(field('first_name').eq('Jane'))
        ).and_(
            field('last_login').is_not_null()
        )
        self.assertSql('(username = ? OR first_name = ?) AND last_login IS NOT NULL', expr)
        self.assertParams(('jane', 'Jane'), expr)


if __name__ == '__main__':
    unittest.main()
