import csv


def file_csv_import(path, expansion):
    lst = []
    try:
        with open(f"{path}.{expansion}", "r", encoding="utf8") as file:
            file_csv = csv.reader(file, delimiter=";", lineterminator="\r")
            for row in file_csv:
                lst.append(row)
        return tuple(lst)
    except FileNotFoundError:
        print("Файл не существует")
        return lst


def file_csv_export(data):
    with open("db_export_file.csv", "w", encoding="utf8") as file:
        file_csv = csv.writer(file, delimiter=";", lineterminator="\r")
        file_csv.writerows(data)
