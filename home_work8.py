# Задача 1
# Задан некоторый список A содержащий целые числа.
# Используя инструкцию while разработать программу, которая вычисляет сумму элементов списка.
num_list = [34, 785, -24, 0, 5378, -3478, 97, 623]
index = 0
tot_sum = 0
while index < len(num_list):
    tot_sum += num_list[index]
    index += 1
print(f"Сумма элементов списка {num_list} равна {tot_sum}.")

# Задача 2
# Задано число a (1<a<1.5). Из чисел 1+1/2, 1+1/3, 1+1/4 …, напечатать те, которые не меньше a
print("1 < a < 1.5")
a = float(input("Введите значение а = "))
n = 2
b = 1 + 1/n
while b > a:
    print(f"Число {str(b)} не меньше числа a = {str(a)}")
    n += 1
    b = 1 + 1/n

# Задача 3
# Задан список строк. В каждой строке подсчитать количество вхождений заданного любого символа
words = ['one', 'two', 'three', 'four', 'fife', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
symbol = input("Введите символ: ")

for word in words:
    if symbol in word:
        print(f"Количество вхождений символа '{symbol}' в строке '{word}' равняется {word.count(symbol)}. ")

# Задача 4
# Пользователь вводит число.
# Определение наличия заданного элемента в списке list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5].
# Если элемент не найден, то выводится соответствующее сообщение.
num_list = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
user_numb = int(input("Введите число: "))
if user_numb in num_list:
    print(f"Число {str(user_numb)} есть в списке {num_list}.")
else:
    print(f"Числа {str(user_numb)} нет в списке {num_list}.")

# Задача 5
# Рассмотреть методы тюплов из пространства имен
print(dir((48, 67, )))

# Метод'count' возвращает количество появлений значения-аргумента в кортеже
fruits = ("banana", "cherry", "apple", "banana", "cherry")
print(fruits.count("banana"))

# Метод 'index' найдет первое вхождение значения-аргумента и вернет его индекс:
print(fruits.index("cherry"))
