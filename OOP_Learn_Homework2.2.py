import pprint


def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    """
    Формирует список покупок для заданных блюд и количества персон.

    :param dishes: Список названий блюд.
    :param person_count: Количество персон.
    :param cook_book: Словарь с рецептами.
    :return: Словарь с ингредиентами и их общим количеством.
    """
    shop_list = {}

    for dish in dishes:
        # Проверяем, есть ли запрашиваемое блюдо в нашей кулинарной книге
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                # Считаем нужное количество для всех персон
                quantity = ingredient['quantity'] * person_count

                # Если ингредиент уже есть в списке покупок, просто прибавляем количество
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                # Если ингредиента еще нет, создаем для него новую запись
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Внимание: Блюдо '{dish}' не найдено в кулинарной книге.")

    return shop_list


# Пример того, как связать первую и вторую задачу в основном коде:
def main():
    # 1. Сначала получаем cook_book из файла (функция из предыдущей задачи)
    # Для примера я задам его вручную, чтобы можно было сразу запустить код
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
        ]
    }

    # 2. Вызываем новую функцию
    dishes_to_cook = ['Запеченный картофель', 'Омлет']
    persons = 2

    shopping_cart = get_shop_list_by_dishes(dishes_to_cook, persons, cook_book)

    # 3. Выводим результат
    print("Список покупок:")
    pprint.pprint(shopping_cart, sort_dicts=False)


if __name__ == '__main__':
    main()