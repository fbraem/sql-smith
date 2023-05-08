import unittest

from sql_smith.functions import search
from .sql_test_case import SqlTestCase


class LikeTests(SqlTestCase):
    def test_begins(self) -> None:
        expr = search("username").begins("sal")
        self.assertSql("username LIKE ?", expr)
        self.assertParams(("sal%",), expr)

        expr = search("username").not_begins("kim")
        self.assertSql("username NOT LIKE ?", expr)
        self.assertParams(("kim%",), expr)

    def test_contains(self) -> None:
        expr = search("username").contains("ill")
        self.assertSql("username LIKE ?", expr)
        self.assertParams(("%ill%",), expr)

        expr = search("username").not_contains("ar")
        self.assertSql("username NOT LIKE ?", expr)
        self.assertParams(("%ar%",), expr)

    def test_ends(self) -> None:
        expr = search("username").ends("ly")
        self.assertSql("username LIKE ?", expr)
        self.assertParams(("%ly",), expr)

        expr = search("username").not_ends("am")
        self.assertSql("username NOT LIKE ?", expr)
        self.assertParams(("%am",), expr)


if __name__ == "__main__":
    unittest.main()
