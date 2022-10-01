import user_interface as ui
import database as db
import model_csv
import model_txt
import os


def select_processing():
    while True:
        print("\nГлавное меню")
        """ Обработка главного меню """
        select_main_menu = ui.main_menu()
        if select_main_menu == 1:
            os.system("cls")
            select_record_processing(ui.menu_operation())
        elif select_main_menu == 2:
            os.system("cls")
            ui.show_result(db.read_db())
        elif select_main_menu == 3:
            os.system("cls")
            db.delete_db()
        elif select_main_menu == 4:
            os.system("cls")
            processing_import_menu(
                ui.menu_import(),
                ui.selecting_file().split(".")
            )
        elif select_main_menu == 5:
            os.system("cls")
            expansion = ui.menu_record_extension()
            export_file(expansion)
        else:
            exit()


def select_record_processing(item):
    """ Обработка меню работы с записью """
    if item == 1:
        data = ui.entry_record_data()
        db.insert_one_entry_db(data)
    elif item == 2:
        db.update_one_entry_db(
            ui.entry_record_data(),
            ui.up_del_user(db.read_db())
        )
    else:
        db.delete_one_entry(ui.up_del_user(db.read_db()))


def processing_import_menu(menu, path):
    """ Обработка меню импорта """
    try:
        data = import_file(path[0], path[1])
        if menu == 1:
            db.delete_insert_db(data)
        else:
            db.insert_db(data)
    except IndexError:
        print("Не правильное имя файла")


def import_file(path, expansion):
    """ Обработка файла для импорта """
    if expansion == "csv":
        return model_csv.file_csv_import(path, expansion)
    elif expansion == "txt":
        return model_txt.file_txt_import(path, expansion)
    else:
        print("Файл не поддерживается.")


def export_file(expansion):
    """ Обработка файла для экспорта' """
    data = db.read_db()
    if expansion == 1:  # txt
        model_txt.file_txt_export(data)
    elif expansion == 2:  # csv
        model_csv.file_csv_export(data)
