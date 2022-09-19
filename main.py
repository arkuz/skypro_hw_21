from courier import Courier
from request import Request
from shop import Shop
from store import Store

store1 = Store({
    'яблоко': 5,
    'банан': 8,
    'абрикос': 7,
    'персик': 12,
    'печенье': 5,
    'молоко': 3,
})
store2 = Store({
    'яблоко': 6,
    'банан': 2,
    'абрикос': 2,
    'персик': 1,
    'печенье': 19,
    'молоко': 3,
})
shop1 = Shop({
    'яблоко': 1,
    'банан': 2,
    'абрикос': 2,
    'персик': 2,
})
shop2 = Shop({})

shops = {
    'магазин': shop1,
    'пвз': shop2,
}

stores = {
    'склад': store1,
    'хранилище': store2,
}

all_units = {**stores, **shops}


def run():
    while True:
        user_input = input('Пользовательский ввод: пример: "Доставить 3 молоко из склад в магазин"\n').lower()
        if user_input == 'стоп':
            return

        try:
            request = Request(user_input)
        except ValueError:
            print('Неудалось распарсить запрос. Повторите ввод:\n')
            continue

        courier = Courier(request, {**stores, **shops})

        print(f"На {request.from_} до: {all_units[request.from_].get_items()}")
        print(f"В {request.to} до: {all_units[request.to].get_items()}")

        try:
            courier.pull()
        except ValueError:
            print('Невозможно забрать такое количество. Повторите ввод:\n')
            continue

        try:
            courier.push()
        except ValueError:
            print('Ошибка при перемещении товара в магазин. Повторите ввод:\n')
            continue

        print(f"На {request.from_} после: {all_units[request.from_].get_items()}")
        print(f"В {request.to} после: {all_units[request.to].get_items()}")


if __name__ == '__main__':
    run()
