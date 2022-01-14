# Задача 1
# Рассмотреть метод sort. Проработать и сделать свои примеры
# По умолчанию - сортировка по возрастанию (reverse=False) алфавита или по возрастанию чисел
list_1 = ["tomato", "carrot", "potato", "onion", "cucumber"]
list_1.sort()
print(list_1)
list_1.sort(reverse=True)
print(list_1)

list_2 = [-589, 98, 0, -0.2857, 2548, 45]
list_2.sort()
print(list_2)
list_2.sort(reverse=True)
print(list_2)

# Заглавные буквы < строчных:
list_3 = ["tomato", "carrot", "POtato", "onion", "Cucumber"]
list_3.sort()
print(list_3)

# Цифры (тип - str) < строк
list_4 = ["2940", "tomato", "0.9", "-584", "carrot", "POato", "45", "onion", "-0.58", "Cucumber"]
list_4.sort()
print(list_4)

# Вот тут вопрос: почему пайтон считает строковый объект "-1.4" самым маленьким?
list_5 = ["5", "-6", "-1.4", "0", "3.8", "-6.4", "7.9", "5.0"]
list_5.sort()
print(list_5)

# symbol  < numbers < english letters < russian letters
list_6 = ["!", "sfgng", "еапмву", "456"]
list_6.sort()
print(list_6)

# В качестве ключа можно использовать встроенные функции python:
list_6 = ["tomato", "carrot", "potato", "onion", "cucumber"]
list_6.sort(key=len)
print(list_6)

list_7 = ['101.0', '20.9', '13.4', '-106.4']
list_7.sort(key=float)
print(list_7)

# Задача 2
# Реализовать копирование списков через “spred” оператор, и конструктор list(). Проверить id

# Spread-оператор делает поверхностную копию списка.
fruits = ['apple', 'banana', 'melon', 'pineapple']
fr = [*fruits]
print("fr: -----", fr, ". Type of fr is: -----", type(fr))
print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
print("fr: -----", id(fr))
print("fruits: -----", id(fruits))
print("fr[1]: -----", id(fr[2]))
print("fruits[1]: -----", id(fruits[2]))

# Конструктор list() делает также поверхностную копию списка.
fruits = ['apple', 'banana', 'melon', 'pineapple']
fr = list(fruits)
print("fr: -----", fr, ". Type of fr is: -----", type(fr))
print("fruits: -----", fruits, ". Type of fruits is: -----", type(fruits))
print("fr: -----", id(fr))
print("fruits: -----", id(fruits))
print("fr[1]: -----", id(fr[2]))
print("fruits[1]: -----", id(fruits[2]))

# Задача 3
# Задана строка “sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;”.
# Создать список, который содержит только цифри.
str_obj = "sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;"
list_obj1 = []
for symbol in str_obj:
    if symbol.isdigit():
        list_obj1.append(symbol)
print(f"Список, состоящий только из цифр, выглядит так: {list_obj1}")
# или с помощью list comprehension:
list_obj2 = [symbol for symbol in str_obj if symbol.isdigit()]
print(f"Список, состоящий только из цифр, выглядит так: {list_obj2}")

# Задача 4
# Задан список: [121, 544, 111, 99, 77]. Создать список, элементы которого делятся на 11
num_list = [121, 544, 111, 99, 77]
new_list = []
for num in num_list:
    if num % 11 == 0:
        new_list.append(num)
print(new_list)
# или с помощью list comprehension:
new_list2 = [num for num in num_list if num % 11 == 0]
print(new_list2)

# Задача 5
# Имеется начальный список цен на изделия. Сегодня на них дана скидка 10 %. Составить новый с учетом удешевления стоимости.
prices = [2400, 1200, 5600, 7010, 399, 470, 2800, 3456]
new_prices = [(price - 10 * (price / 100)) for price in prices]
print(f"Новый список цен с учетом скидки 10% выглядит так: {new_prices}")


# Задача 6
# Задан список фруктов ['apple', ‘pear’, 'banana', 'melon', 'pineapple'].
# Создать список, если слово начинается с буквы “р”, добавить к слову “my ”.
# Нужно получить такой список ['my pear', 'my pineapple']
fruits = ["apple", "pear", "banana", "melon", "pineapple"]
new_fruits = [f"my {fruit}" for fruit in fruits if fruit.startswith("p")]
print(new_fruits)