print("Вас приветствует программа по приготовлению блюда")
print("От вас потребуется список продуктов из рецепта")
print("И перечень имеющихся в холодильнике")
user_answer = input("Желаете продолжить? (да/нет) ")
recipe = {}
s_list = {}
flag = 0
refrigerator_dic = {}
while user_answer != "нет":
    k = input("Введите название продукта: ")
    v = int(input("Введите количество: "))
    recipe.update({k: v})
    user_answer = input("Продолжить? (да/нет): ")
print("Отлично! Рецепт находится в моей памяти")
print("Переходим к осмотру холодильника!")
refrigerator = list(recipe.keys())
for i in refrigerator:
    print("Продукт: ", i)
    v = int(input("Введите количество: "))
    refrigerator_dic.update({i: v})
for i in recipe:
    if refrigerator_dic[i] < recipe[i]:
        v = recipe[i] - refrigerator_dic[i]
        s_list.update({i: v})
    elif refrigerator_dic[i] >= recipe[i]:
        flag += 1;
if flag == len(recipe):
    print("Ничего покупать не нужно")
for i in s_list:
    print("Нужно купить:", i, "-", s_list[i], end=" \n")
