import unittest

from sql_smith.engine.postgres_engine import PostgresEngine
from .sql_test_case import SqlTestCase


class PostgresInsertTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> "EngineInterface":
        return PostgresEngine()

    def test_returning(self) -> None:
        insert = self._factory.insert("users", {"username": "james"}).returning("id")

        self.assertSql(
            'INSERT INTO "users" ("username") VALUES (%s) RETURNING "id"', insert
        )
        self.assertParams(("james",), insert)


if __name__ == "__main__":
    unittest.main()
