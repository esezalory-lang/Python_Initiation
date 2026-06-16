#!/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self: "DataProcessor") -> None:
        self.rank_tracker = 0
        self.data_storage = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        len = 0
        for i in self.data_storage:
            len += 1
        current_rank = self.rank_tracker - len
        current_value = self.data_storage[0]
        self.data_storage.remove(self.data_storage[0])
        return (current_rank, current_value)


class NumericProcessor(DataProcessor):
    def __init__(self: "NumericProcessor") -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        data_types = (int, float, list)
        list_types = (int, float)

        if isinstance(data, data_types):
            if isinstance(data, list):
                if not all(isinstance(i, list_types) for i in data):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]
               ) -> None:
        if self.validate(data) is False:
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.data_storage += str(i)
                    self.rank_tracker += 1
            else:
                self.data_storage += str(data)
                self.rank_tracker += 1


class TextProcessor(DataProcessor):
    def __init__(self: "TextProcessor") -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        data_types = (str, list)

        if isinstance(data, data_types):
            if isinstance(data, list):
                if not all(isinstance(i, str) for i in data):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is False:
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.data_storage += [str(i)]
                    self.rank_tracker += 1
            else:
                self.data_storage += str(data)
                self.rank_tracker += 1


class LogProcessor(DataProcessor):
    def __init__(self: "LogProcessor"):
        super().__init__()

    def validate(self, data: Any) -> bool:
        data_types = (dict, list)

        if isinstance(data, data_types):
            if isinstance(data, dict):
                if not all(isinstance(key, str) and isinstance(value, str)
                           for key, value in data.items()):
                    return False
            elif isinstance(data, list):
                for index in data:
                    if not all(isinstance(key, str) and isinstance(value, str)
                               for key, value in index.items()):
                        return False
            return True
        else:
            return False

    def ingest(self, data: dict | list[dict]) -> None:
        if self.validate(data) is False:
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for i in data:  # level 1
                    to_join = ""
                    len = 0
                    for j, k in i.items():
                        to_join += k
                        if len == 0:
                            to_join += ": "
                        len += 1
                    self.data_storage += [to_join]
                    self.rank_tracker += 1
            else:
                for key, value in data.items():
                    self.data_storage += [str(key) + ": " + str(value)]
                    self.rank_tracker += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    