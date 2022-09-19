from base_classes import Storage
from request import Request


class Courier:
    def __init__(self, request: Request, storages: dict[str, Storage]):
        self._request = request
        self._storages = storages

    def _check_storage(self):
        return self._request.from_ in self._storages

    def _check_shop(self):
        return self._request.to in self._storages

    def pull(self):
        if self._check_storage():
            self._storages[self._request.from_].remove(self._request.product,
                                                       self._request.amount)
            print(f'Курьер забирает из {self._request.from_} {self._request.amount} {self._request.product}')
        else:
            raise ValueError(f'Storage {self._request.from_} are not exist')

    def push(self):
        if self._check_shop():
            self._storages[self._request.to].add(self._request.product,
                                                 self._request.amount)
            print(f'Курьер доставляет в {self._request.to} {self._request.amount} {self._request.product}')

        else:
            raise ValueError(f'Storage {self._request.to} are not exist')

    def rollback(self):
        self._storages[self._request.to].add(self._request.product,
                                             self._request.amount)
        print(f'Курьер отменил доставку {self._request.amount} {self._request.product} '
              f'из {self._request.from_} в {self._request.to} ')
