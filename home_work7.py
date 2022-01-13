#  Задача 1
# Рассмотреть метод sort. Проработать и сделать свои примеры



# Задача 2
# Реализовать копирование списков через “spred” оператор, и конструктор list(). Проверить id



# # Задача 3
# # Задана строка “sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;”.
# # Создать список, который содержит только цифри.
# str_obj = "sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE;"
# list_obj1 = []
# for symbol in str_obj:
#     if symbol.isdigit():
#         list_obj1.append(symbol)
# print(f"Список, состоящий только из цифр, выглядит так: {list_obj1}")
# # или с помощью list comprehension:
# list_obj2 = [symbol for symbol in str_obj if symbol.isdigit()]
# print(f"Список, состоящий только из цифр, выглядит так: {list_obj2}")

# # Задача 4
# # Задан список: [121, 544, 111, 99, 77]. Создать список, элементы которого делятся на 11
# num_list = [121, 544, 111, 99, 77]
# new_list = []
# for num in num_list:
#     if num % 11 == 0:
#         new_list.append(num)
# print(new_list)
# # или с помощью list comprehension:
# new_list2 = [num for num in num_list if num % 11 == 0]
# print(new_list2)

# # Задача 5
# # Имеется начальный список цен на изделия. Сегодня на них дана скидка 10 %. Составить новый с учетом удешевления стоимости.
# prices = [2400, 1200, 5600, 7010, 399, 470, 2800, 3456]
# new_prices = [0.9 * price for price in prices]
# print(f"Новый список цен с учетом скидки 10% выглядит так: {new_prices}")

# # Задача 6
# # Задан список фруктов ['apple', ‘pear’, 'banana', 'melon', 'pineapple'].
# # Создать список, если слово начинается с буквы “р”, добавить к слову “my ”.
# # Нужно получить такой список ['my pear', 'my pineapple']
# fruits = ["apple", "pear", "banana", "melon", "pineapple"]
# new_fruits = [str("my ") + fruit for fruit in fruits if fruit.startswith("p")]
# print(f"Новый список объектов, которые начинаются на букву 'p', с дополнением словом 'my' выглядит так: {new_fruits}")
