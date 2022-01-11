# # Задача 1.
# # Изучить методы пространсва имен списков.
# # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# print(dir([]))
# names = ["Oliver", "Adam", "Daniel", "Scott", "Jack", "John", "Steven", "Adam"]
# print(names)
#
# # Метод .append(item) добавляет объект в конец списка
# names.append("Oscar")
# print(names)
#
# # Метод .copy копирует список
# names_2 = names.copy()
# print(f" Lists names_2 is {names_2}")
#
# # Метод .extend(name_list) добавляет элементы списка name_list в конец другого списка
# names_3 = ["Mary", "Alice", "Kathy"]
# names_2.extend(names_3)
# print(names_2)
#
# # Метод .insert(index, item) добавляет элемент item в список по индексу index
# names.insert(4, "Samuel")
# print(names)
#
# # Метод .index(item) возвращает индекс первого вхождения элемента item
# print(names.index("Adam"))
#
# # Метод .remove(item) удаляет первое вхождение элемента item
# names.remove("Daniel")
# print(names)
#
# # Метод .pop([index]) удаляет и возвращает элемент по индексу index.
# print(names.pop(-4))
# # Если индекс не передан, то просто удаляет последний элемент.
# print(names.pop())
#
# # Метод .count(item) возвращает количество вхождений элемента item в список
# print(names.count("Adam"))
#
# # Метод .sort([key]) сортирует элементы
# names.sort()
# print(names)
#
# # Метод .reverse() делает реверс списка
# names.reverse()
# print(names)
#
# # Метод .clear()удаляет все элементы из списка
# names.clear()
# print(names)
#
#
# Задача 2.
# Имеется два списка. Проверить, все ли элементы втрого списка присутствуют в первом списке.
# Эту задачу можно сделать многими пособами. Найти самый короткий


# # Задача 3.
# # Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
# zero_list = [0] * 100
# zero_list.insert(0, 1)
# zero_list.append(1)
# print(zero_list)
# print(len(zero_list))

# # Задача 4.
# # Сформировать возрастающий список из чётных чисел (количество элементов 45)
# # Вариант 1
# even_numbers = list(range(2,91,2))
# print(even_numbers)
# print(f"Длина списка первым методом {len(even_numbers)}")
#
# # Вариант 2
# even_numbers_1 = []
# for n in range(1,1000):
#     if n%2 == 0 and len(even_numbers_1) < 45:
#             even_numbers_1.append(n)
# print(even_numbers_1)
# print(f"Длина списка вторым методом {len(even_numbers_1)}")
#

# # Задача 5.
# # Пользователь вводит число. Определить, содержит ли список данное число x.
# # Вивести информационное сообщение содержит или не содержит
# numbers_5 = list(range(0, 100, 4))
# print("Введите число x, чтобы проверить, есть ли оно в списке.")
# number = int(input("x = "))
# print(f"Список выглядит так: {numbers_5}")
# if number in numbers_5:
#     print(f"Он содержит число {number}.")
# else:
#     print(f"Он не содержит число {number}.")
#
#
# # Задача 6.
# # Найдите сумму и произведение элементов списка. Результаты вывести на экран
# numbers_6 = list(range(1,15,3))
# print(f"Список выглядит так: {numbers_6}")
# print(f"Сумма элементов этого списка = {sum(numbers_6)}")
#
# prodacts = 1
# for x in numbers_6:
#     prodacts = prodacts*x
# print(f"Произведение элементов этого списка = {prodacts}")
#
# Задача 7.
# Найти наибольший элемент списка и вывести его на экран
# numbers_7 = [123, -5, 0.456, 24796, -7592, 4, -0.9345, 345, -75]
# print(f"Наибольшим элементом списка {numbers_7} является элемент {max(numbers_7)}")
#
# Задача 8.
# Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение
#
# names_8 = ["Jack", "Oliver", "Adam", "Jack", "Daniel", "Scott", "Jack", "John", "Steven", "Adam"]
# for i in range(len(names_8)):
#     if int(names_8.count(i))>1:
#
#
# print(f"Элемент {name} в списке {names_8} встречается {str(names_8.count(name))} раз")
#
#

# # Задача 9.
# # Поменять местами самый большой и самый маленький элементы списка
# # Вариант 1.
# numbers_9 = [123, -5, 0.456, 24796, 4, -0.9345,-7592, 345, -75]
# print(f"Список : {numbers_9}")
#
# n_max = max(numbers_9)
# n_min = min(numbers_9)
#
# index_max = numbers_9.index(n_max)
# index_min = numbers_9.index(n_min)
#
# numbers_9.pop(index_min)
# numbers_9.insert(index_min, n_max)
# numbers_9.pop(index_max)
# numbers_9.insert(index_max, n_min)
#
# print(f"Так выглядит список, где самое большое и самое маленькое значения поменяли местами: {numbers_9}")
#
# # Вариант 2
# numbers_9 = [123, -5, 0.456, 24796, 4, -0.9345,-7592, 345, -75]
# print(f"Список : {numbers_9}")
# maximum = max(numbers_9)
# print(maximum)
# minimum = min(numbers_9)
# print(minimum)
# for i in range(len(numbers_9)):
#     if numbers_9[i] == maximum:
#         numbers_9[i] = minimum
#     elif numbers_9[i] == minimum:
#         numbers_9[i] = maximum
# print(f"Так выглядит список, где самое большое и самое маленькое значения поменяли местами: {numbers_9}")

# # Задача 10.
# # Дан произвольный список. Представьте его в обратном порядке
# numbers_10 = [123, -5, 0.456, 24796, 4, -0.9345,-7592, 345, -75]
# numbers_10.reverse()
# print(numbers_10)
