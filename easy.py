import os


def construct():
    s = input("Введите название папки: ")
    full_path = os.path.join(os.getcwd(), s)
    if os.path.exists(full_path):
        return full_path
    else:
        print("Папки не существует")
        return -1


def cd_dir():
    full_path = construct()
    if full_path != -1:
        os.chdir(full_path)
        print(os.getcwd())


def dir_list():
    full_path = construct()
    if full_path != -1:
        print("Содержимое директории ", full_path)
        print(os.listdir(full_path))


def dir_rm():
    full_path = construct()
    if full_path != -1:
        os.rmdir(full_path)
        print("Папка удалена")


def dir_mk():
    s = input("Введите название папки: ")
    full_path = os.path.join(os.getcwd(), s)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print("Папка создана!")
    else:
        print("Папка уже существует")
