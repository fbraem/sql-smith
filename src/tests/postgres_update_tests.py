import unittest

from sql_smith.engine.postgres_engine import PostgresEngine
from .sql_test_case import SqlTestCase


class PostgresUpdateTests(SqlTestCase):
    @classmethod
    def get_engine(cls) -> 'EngineInterface':
        return PostgresEngine()

    def test_returning(self) -> None:
        update = self._factory \
            .update('users', {'is_active': False, 'last_login': None}) \
            .returning('id')

        self.assertSql('UPDATE "users" SET "is_active" = false, "last_login" = NULL RETURNING "id"', update)
        self.assertParams((), update)


if __name__ == '__main__':
    unittest.main()
