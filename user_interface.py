def main_menu():
    """ Глдавное меню программы """
    menu = [
        "Обработать данные",
        "Прочитать данные",
        "Удалить данные",
        "Загрузить данные",
        "Выгрузить данные",
        "Выход",
    ]
    return selecting_item(menu)


def menu_operation():
    """ Меню работы с записью """
    menu = [
        "Создать запись",
        "Изменить запись",
        "Удалить запись",
    ]
    return selecting_item(menu)


def menu_import():
    """ Меню работы с записью """
    menu = [
        "Загрузить с заменой",
        "Загрузить с добавлением",
    ]
    return selecting_item(menu)


def menu_record_extension():
    """ Меню выбора расширения экспорта и импорта """
    print("Выберите расширение:")
    record_extensions = ["txt", "csv", ]
    return selecting_item(record_extensions)


def show_result(data):
    """ Функция вывода на экран """
    for item in data:
        print(*item)


def selecting_file():
    path = input("Введите имя файла: ")
    return path


def selecting_item(date_menu):
    """ Функция обработки выбора меню """
    for item in enumerate(date_menu, 1):
        print(item[0], item[1])
    while True:
        try:
            item_number = int(input("Выберите пункт меню: "))
            if 1 <= item_number <= len(date_menu):
                return item_number
            else:
                raise ValueError
        except ValueError:
            print("Выберите правильный пункт меню")


def entry_record_data():
    """ Ввод данных записи """
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    post = input("Введите должность: ")
    record = [name, surname, post]
    return record


def up_del_user(data):
    """ Выбор номера записи """
    while True:
        try:
            num = int(input("Введите номер записи для изменения: "))
            if 0 < num <= len(data):
                return num
            else:
                raise ValueError
        except ValueError:
            print("Введите правильное число:")
