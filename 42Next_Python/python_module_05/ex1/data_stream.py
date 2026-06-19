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
        len = len(self.data_storage)
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


class DataStream:
    def __init__(self: "DataStream"):
        self.polyphorm: DataProcessor = DataProcessor()
        self.processors = []

    # register new dataprocessor
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for i in stream:
            if len(self.processors) == 0:
                raise Exception("No processor found, no data")
            for processor in self.processors:
                if not processor.validate(i):
                    raise Exception("DataStream error -",
                                    f"Can't process element in stream: {i}")
                else:
                    break
            processor.ingest(i)

    def print_processor_stats(self) -> None:
        if len(self.processors) == 0:
            print("No processor found, no data")
        else:
            for i in self.processors:
                



if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data = ['Hello world', [3.14, -1, 2.71],
            [
            {'log_level': 'WARNING', 'log_message':
             'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message':
             'User wil is connected'}
            ],
            42, ['Hi', 'five']]
    
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data_stream = DataStream()

    print("== DataStream statistics ==")
    data_stream.print_processor_stats()

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(numeric)
    print("Send first batch of data on stream: ['Hello world', [3.14, -1, 2.71],",
          "[{'log_level': 'WARNING', 'log_message':",
          " 'Telnet access! Use ssh instead'},", 
          "{'log_level': 'INFO', 'log_message':",
          "'User wil is connected'}], 42, ['Hi', 'five']]")
    try:
        data_stream.process_stream(data)
    except Exception as e:
        print(f"{e}")