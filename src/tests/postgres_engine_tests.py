import unittest

from sql_smith.engine.postgres_engine import PostgresEngine
from sql_smith.functions import identify
from .sql_test_case import SqlTestCase


class PostgresEngineTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> "EngineInterface":
        return PostgresEngine()

    def test_identifier(self) -> None:
        f = identify("id")
        self.assertSql('"id"', f)


if __name__ == "__main__":
    unittest.main()
