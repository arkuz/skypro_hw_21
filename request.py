class Request:
    _from: str
    _to: str
    _amount: int
    _product: str

    def __init__(self, request_string: str):
        # Пример "Доставить 3 печеньки из склад в магазин"
        splitted = request_string.split()
        if len(splitted) != 7:
            raise ValueError('Parse arguments != 7')

        self._amount = int(splitted[1])
        self._product = splitted[2]
        self._from = splitted[4]
        self._to = splitted[6]

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product
