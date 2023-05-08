import unittest

from sql_smith.functions import func, param
from .sql_test_case import SqlTestCase


class IssueTests(SqlTestCase):
    """
    These are tests that were created to solve issues in the original PHP library Latitude.
    To be sure that the port to Python is ok, these tests are also ported.
    """

    def test_func_columns(self) -> None:
        expr = func("COUNT", "id")

        self.assertSql("COUNT(id)", expr)
        self.assertParams((), expr)

    def test_func_params(self) -> None:
        expr = func("POINT", param(1), param(2))

        self.assertSql("POINT(?, ?)", expr)
        self.assertParams((1, 2), expr)

    def test_reset_limit(self) -> None:
        query = self._factory.select().from_("users").limit(5).limit(None)

        self.assertSql("SELECT * FROM users", query)

    def test_reset_offset(self) -> None:
        query = self._factory.select().from_("users").offset(5).offset(None)

        self.assertSql("SELECT * FROM users", query)

    def test_select_star(self) -> None:
        query = self._factory.select().from_("users")

        self.assertSql("SELECT * FROM users", query)

    def test_select_replace_columns(self) -> None:
        query = self._factory.select().columns("id").from_("users")
        self.assertSql("SELECT id FROM users", query)

    def test_select_add_columns(self) -> None:
        query = self._factory.select().add_columns("id", "username").from_("users")
        self.assertSql("SELECT id, username FROM users", query)

    def test_select_replace_table(self) -> None:
        query = self._factory.select().from_("users").from_("posts")
        self.assertSql("SELECT * FROM posts", query)

    def test_select_append_table(self) -> None:
        query = self._factory.select().from_("users").add_from("posts")
        self.assertSql("SELECT * FROM users, posts", query)


if __name__ == "__main__":
    unittest.main()
