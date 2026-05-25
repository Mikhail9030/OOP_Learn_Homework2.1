import pprint


def parse_recipes_file(file_path: str) -> dict:
    """
    Читает файл с рецептами и возвращает словарь cook_book.

    :param file_path: Путь к текстовому файлу с рецептами.
    :return: Словарь с блюдами и списком их ингредиентов.
    """
    cook_book = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                # Читаем название блюда
                dish_name = file.readline().strip()

                # Если строка пустая, значит мы дошли до конца файла
                if not dish_name:
                    break

                # Читаем количество ингредиентов
                ingredients_count = int(file.readline().strip())

                ingredients = []
                for _ in range(ingredients_count):
                    # Читаем строку ингредиента и разбиваем её по разделителю " | "
                    ingredient_line = file.readline().strip()
                    item_name, quantity, measure = ingredient_line.split(' | ')

                    # Добавляем словарь ингредиента в список
                    ingredients.append({
                        'ingredient_name': item_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })

                # Добавляем готовый список в кулинарную книгу
                cook_book[dish_name] = ingredients

                # Читаем пустую строку между рецептами
                file.readline()

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except ValueError as e:
        print(f"Ошибка при обработке данных файла: {e}")

    return cook_book


def main():
    # Имя файла с рецептами (предполагается, что он лежит в той же папке)
    filename = 'Cooking Book/recipes.txt'

    # Получаем словарь с рецептами
    cook_book = parse_recipes_file(filename)

    # Красиво выводим результат в консоль
    if cook_book:
        print("cook_book = ")
        pprint.pprint(cook_book, sort_dicts=False)


if __name__ == '__main__':
    main()