import unittest
from sql_smith.functions import identify, alias
from sql_test_case import SqlTestCase


class IdentifierTests(SqlTestCase):
    def test_identity(self) -> None:
        field = identify('id')
        self.assertSql('id', field)
        self.assertParams((), field)

    def test_alias(self) -> None:
        table_alias = alias('users', 'u')
        self.assertSql('users AS u', table_alias)
        self.assertParams((), table_alias)

    def test_qualified(self) -> None:
        field = identify('public.users.username')
        self.assertSql('public.users.username', field)
        self.assertParams((), field)

    def test_qualified_alias(self) -> None:
        field_alias = alias('u.id', 'user_id')
        self.assertSql('u.id AS user_id', field_alias)
        self.assertParams((), field_alias)


if __name__ == '__main__':
    unittest.main()
