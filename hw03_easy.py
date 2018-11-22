def my_round(number, n_digits):
  return int(number * 10**n_digits + 0.49) / 10**n_digits


def lucky_ticket(ticket: int):
    if len(str(ticket)) == 6:
        two_left_number = ticket // 10000
        two_right_number = ticket % 100
        if two_left_number % 10 + two_left_number // 10 == two_right_number % 10 + two_right_number // 10:
            return "Билет счастливый"
        else:
            return "Билет несчастливый"
    else:
        return "В билете не 6 цифр"


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print(lucky_ticket(123506))
print(lucky_ticket(123212))
print(lucky_ticket(426751))
