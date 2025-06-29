"""
Есть класс, предоставляющий доступ к набору чисел.
Источником этого набора чисел является некоторый
файл. С определенной периодичностью данные в файле
меняются (надо реализовать механизм обновления).
Приложение должно получать доступ к этим данным и
выполнять набор операций над ними (сумма, максимум,
минимум и т.д.). При каждой попытке доступа к этому
набору необходимо вносить запись в лог-файл. При реализации используйте
паттерн Proxy (для логгирования)
и другие необходимые паттерны.
"""
from abc import ABC, abstractmethod
import time
import os


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass


class Data(DataSource):
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.last_modified = 0
        self.load_data()

    def load_data(self):
        if self.filename and os.path.exists(self.filename):
            current_modified = os.path.getmtime(self.filename)
            if current_modified > self.last_modified:
                self.data = []
                with open(self.filename, 'r') as f:
                    for line in f:
                        for part in line.strip().split():
                            try:
                                number = float(part)
                                self.data.append(number)
                            except ValueError:
                                print(f"Ошибка: '{part}' не число")
                self.last_modified = current_modified
        else:
            self.data = []

    def get_data(self):
        self.load_data()
        return self.data


class DataProxy(DataSource):
    def __init__(self, filename):
        self.filename = filename
        self._real_data = None

    def load_data(self):
        if self._real_data is None:
            self._real_data = Data(self.filename)
        self._real_data.load_data()
        self.log("Данные загружены")

    def get_data(self, strategy=None):
        if self._real_data is None:
            self.load_data()
        data = self._real_data.get_data()
        self.log(f"Доступ к данным с помощью {strategy.__class__.__name__}")
        return data

    def log(self, message):
        with open('2/log.txt', 'a', encoding='utf-8') as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {message}\n")


class DataStrategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class SumStrategy(DataStrategy):
    def execute(self, data):
        return sum(data) if data else 0


class MaxStrategy(DataStrategy):
    def execute(self, data):
        return max(data) if data else None


class MinStrategy(DataStrategy):
    def execute(self, data):
        return min(data) if data else None


class DataProcessor:
    def __init__(self, data_proxy, strategy):
        self.data_proxy = data_proxy
        self.strategy = strategy

    def execute_strategy(self):
        return self.strategy.execute(self.data_proxy.get_data(self.strategy))


if __name__ == "__main__":
    filename = '2/numbers.txt'
    data_proxy = DataProxy(filename)

    sum_strategy = SumStrategy()
    max_strategy = MaxStrategy()
    min_strategy = MinStrategy()

    data_processor = DataProcessor(data_proxy, sum_strategy)
    print(f'Sum: {data_processor.execute_strategy()}')

    data_processor_2 = DataProcessor(data_proxy, max_strategy)
    print(f'Max: {data_processor_2.execute_strategy()}')

    data_processor_3 = DataProcessor(data_proxy, min_strategy)
    print(f'Min: {data_processor_3.execute_strategy()}')
