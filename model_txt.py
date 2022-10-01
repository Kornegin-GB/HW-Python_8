def file_txt_import(path, expansion):
    lst = []
    try:
        with open(f"{path}.{expansion}", "r", encoding="utf8") as file:
            for item in file.readlines():
                lst.append(item.split(", "))
        return lst
    except FileNotFoundError:
        print("Файл не существует")
        return lst


def file_txt_export(data):
    with open("db_export_file.txt", "w", encoding="utf8") as file:
        for t in data:
            line = ', '.join(str(x) for x in t)
            file.write(line.strip() + '\n')
