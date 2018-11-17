# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

import re
import string

text1 = input('Пишите текст только английскими буквами, исключив цифры, разрешенные символы "" ')
text2 = text1.lower().replace(", ", " ").replace(". ", " ").replace(".", "").replace("!", "").replace("?", "").split()
print(text2)
c = len(text2)
print("Слов в тексте: ", c)
text1 = text1.lower().replace(", ", "").replace(". ", "").replace(".", "").replace("!", "").replace("?", "")
text1 = re.sub(r'\s+', '', text1)
text1 = list(text1)  # Преобразуем строку в список для отделения символов
text1C = set(text1)  # Преобразуем список во множество для удаления дублей
text1 = ''.join(i for i in text1C if i in string.ascii_letters) # Преобразуем в строку только латинские буквы
print(text1)
print("Количество использованных букв английского алфвита:", len(text1))

# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра

text1 = input()
text1 = text1.lower().replace(", ", " ").replace(". ", " ").replace(".", "").replace("!", "").replace("?", "").split()

text2 = input()
text2 = text2.lower().replace(", ", " ").replace(". ", " ").replace(".", "").replace("!", "").replace("?", "").split()

text1 = set(text1)
text2 = set(text2)
print(text1.union(text2))
print(text1.intersection(text2))
