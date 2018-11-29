import os
import sys
import shutil


def create_dir():
    print('os.getcwd() = ', os.getcwd())
    i = 1
    while i < 10:
        dir_path = os.path.join(os.getcwd(), "dir_" + str(i))
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            i += 1
        else:
            i += 1


def delete_dir():
    i = 1
    while i < 10:
        dir_path = os.path.join(os.getcwd(), "dir_" + str(i))
        if os.path.exists(dir_path):
            os.rmdir(dir_path)
            i += 1
        else:
            i += 1


def dir_list():
    directory = os.listdir(os.getcwd())
    extensions = set([os.path.splitext(file)[0] for file in directory
                      if not os.path.isfile(os.path.join(os.getcwd(), file))])
    print(extensions)


def copy_file():
    file_name = os.path.basename(sys.argv[0])
    s = os.path.splitext(file_name)[0]
    shutil.copyfile(file_name, s + "_copy" + ".py")
    print(s)

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


create_dir()
delete_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


dir_list()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


copy_file()
