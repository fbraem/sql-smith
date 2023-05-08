from sql_smith.functions import on
from .sql_test_case import SqlTestCase


class CteTests(SqlTestCase):
    def test_cte(self):
        cte = self._factory.select("id").from_("users").order_by("users.id").limit(10)
        select = (
            self._factory.select()
            .with_("limit_users", cte)
            .from_("users")
            .left_join("limit_users", on("limit_users.id", "users.id"))
        )
        self.assertSql(
            "WITH limit_users AS (SELECT id FROM users ORDER BY users.id LIMIT 10) "
            "SELECT * FROM users LEFT JOIN limit_users ON limit_users.id = users.id",
            select,
        )
        self.assertParams((), select)
