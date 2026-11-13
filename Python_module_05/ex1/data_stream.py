from typing import Any, cast
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            items: list[Any] = cast(list[Any], data)
            return all(
                isinstance(i, (int, float)) for i in items
            )
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, (int, float)):
            self.storage.append((self.rank, str(data)))
            self.rank += 1
        else:
            for i in data:
                self.storage.append((self.rank, str(i)))
                self.rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            items: list[Any] = cast(list[Any], data)
            return all(
                isinstance(i, str) for i in items
            )
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, str):
                self.storage.append((self.rank, data))
                self.rank += 1
            if isinstance(data, list):
                items: list[Any] = cast(list[Any], data)
                for i in items:
                    self.storage.append((self.rank, str(i)))
                    self.rank += 1
        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        items: list[Any] = cast(list[Any], data)
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in items
            )
        if isinstance(data, list):
            items = cast(list[dict[str, str]], data)
            return all(
                all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )
                for d in items
            )
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, dict):
            log = f"{data['log_level']}: {data['log_message']}"
            self.storage.append((self.rank, log))
            self.rank += 1
        else:
            for d in data:
                log = f"{d['log_level']}: {d['log_message']}"
                self.storage.append((self.rank, log))
                self.rank += 1


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self.processors:
                if processor.validate(element):
                    try:
                        processor.ingest(element)
                    except Exception as e:
                        print(f"DataStream error - Ingestion failed: {e}")
                    break
            else:
                msg = f"DataStream error - Can't process element: {element}"
                print(msg)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for processor in self.processors:
            total = processor.rank
            remaining = len(processor.storage)
            name = type(processor).__name__
            msg = f"{name}: total {total} items processed, "
            msg += f"remaining {remaining} on processor"
            print(msg)


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[Any] = ['Hello world', [3.14, -1, 2.71],
                        [{'log_level': 'WARNING',
                          'log_message': 'Telnet access! Use ssh instead'},
                         {'log_level': 'INFO',
                          'log_message': 'User wil is connected'}],
                        42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    msg = "\nConsume some elements from the data processors: "
    msg += "Numeric 3, Text 2, Log 1"
    print(msg)
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        stream.processors[1].output()
    for _ in range(1):
        stream.processors[2].output()
    stream.print_processors_stats()
