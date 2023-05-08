from sql_smith.interfaces import StatementInterface


class QualifiedIdentifier(StatementInterface):
    def __init__(self, *args: tuple["StatementInterface"]):
        self._identifiers = args

    def sql(self, engine: "EngineInterface") -> str:
        return engine.flatten_sql(".", *self._identifiers)

    def params(self, engine: "EngineInterface") -> tuple:
        return engine.flatten_params(*self._identifiers)
