from abc import ABC, abstractmethod


class Storage(ABC):
    _items: dict
    _capasity: int

    @abstractmethod
    def add(self, name: str, count: int):
        pass

    @abstractmethod
    def remove(self, name: str, count: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
