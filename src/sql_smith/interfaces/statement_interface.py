from abc import abstractmethod


class StatementInterface:
    @abstractmethod
    def sql(self, engine: "EngineInterface") -> str:
        raise NotImplementedError("sql must be implemented")

    @abstractmethod
    def params(self, engine: "EngineInterface") -> tuple:
        raise NotImplementedError("params must be implemented")
