# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from easy import cd_dir, dir_list, dir_rm, dir_mk
user_answer = ""
while user_answer !="q":
    print("1. Перейти в папку\n"
          "2. Просмотреть содержимое указанной папки\n"
          "3. Удалить папку\n"
          "4. Создать папку\n"
          "Для выхода введите q\n")
    user_answer = input("Введите номер действия\n ")
    if user_answer == "1":
        cd_dir()
    if user_answer == "2":
        dir_list()
    if user_answer == "3":
        dir_rm()
    if user_answer == "4":
        dir_mk()
