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
        length = len(self.data_storage)
        current_rank = self.rank_tracker - length
        current_value = self.data_storage[0]
        self.data_storage.remove(self.data_storage[0])
        return (current_rank, current_value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        data_types = (int, float, list)
        list_types = (int, float)

        if isinstance(data, data_types):
            if isinstance(data, list):
                if not all(isinstance(i, list_types) for i in data):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]
               ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.data_storage.append(str(i))
                    self.rank_tracker += 1
            else:
                self.data_storage.append(str(data))
                self.rank_tracker += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        data_types = (str, list)

        if isinstance(data, data_types):
            if isinstance(data, list):
                if not all(isinstance(i, str) for i in data):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.data_storage.append(str(i))
                    self.rank_tracker += 1
            else:
                self.data_storage.append(str(data))
                self.rank_tracker += 1


class LogProcessor(DataProcessor):
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
        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
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
                    self.data_storage.append(to_join)
                    self.rank_tracker += 1
            else:
                for key, value in data.items():
                    self.data_storage .append(str(key) + ": " + str(value))
                    self.rank_tracker += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f" Trying to validate input '42': {numeric.validate(42)}")
    print(f" Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except Exception as e:
        print(f" Got exception: {e}")
    num_list = [1, 2, 3, 4, 5]
    print(f" Processing data: {num_list}")
    numeric.ingest(num_list)
    print(" Extracting 3 values...")
    for i in range(3):
        output = numeric.output()
        print(f" Numeric value {output[0]}: {output[1]}")
    print()

    print("Testing Text Processor...")
    alpha = TextProcessor()
    str_list = ['Hello', 'Nexus', 'World']
    print(f" Trying to validate input '42': {alpha.validate(42)}")
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    alpha.ingest(str_list)
    print(" Extracting 1 value...")
    output = alpha.output()
    print(f" Text value {output[0]}: {output[1]}")
    print()

    print("Testing Log Processor...")
    logs = LogProcessor()
    log_list = [{'log_level': 'NOTICE',
                 'log_message': 'Connection to server'},
                {'log_level': 'ERROR',
                 'log_message': 'Unauthorized access!!'}]
    print(f" Trying to validate input 'Hello': {logs.validate('Hello')}")
    print("Processing data: ",
          "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'},",
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    logs.ingest(log_list)
    print(" Extracting 2 value...")
    for i in range(2):
        output = logs.output()
        print(f" Log entry {output[0]}: {output[1]}")
