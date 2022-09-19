from typing import Dict

from base_classes import Storage


class Store(Storage):

    def __init__(self, items: Dict[str, int], capasity: int = 100):
        self._items = items
        self._capasity = capasity

    def add(self, name: str, count: int) -> None:
        if len(self._items) + count > self._capasity:
            raise ValueError(f'Not free space in items. {self.get_free_space()} items free')

        if name in self._items:
            self._items[name] += count

        self._items[name] = count

    def remove(self, name: str, count: int) -> None:
        if name in self._items:
            if count > self._items[name]:
                raise ValueError(f'Negative items count: {count} > {self._items[name]}')

            self._items[name] -= count

            if self._items[name] == 0:
                del self._items[name]

    def get_free_space(self) -> int:
        return self._capasity - sum(self._items.values())

    def get_items(self) -> dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items.keys())

    def __repr__(self):
        return f'{Store.__name__}: {self.get_items()}'
