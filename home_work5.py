# Задача 1
# Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.
# print("Введите четное и нечетное числа. ")
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
#
# if num_1 % 2 != 0:
#     print(f"Первое число {num_1} нечетное.")
# elif num_2 % 2 != 0:
#     print(f"Второе число {num_2} нечетное.")

# Задача 2.
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
# num_3 = int(input("Введите третье число: "))
#
# if num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
#     print(f"Второе число {num_2} является средним.")
# elif num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
#     print(f"Первое число {num_1} является средним.")
# elif num_1 < num_3 < num_2 or num_2 < num_3 < num_1:
#     print(f"Третье число {num_3} является средним.")
#
# Задача 3
# Вводятся координаты (x; y) точки и радиус круга (r).
# Определить принадлежит ли данная точка кругу, если его центр находится в начале координат.
# print("Введите координаты точки (x;y)")
# x = int(input("x = "))
# y = int(input("y = "))
# r = int(input("Введите радиус круга r = "))
#
# if (x**2)+(y**2) < r**2:
#     print(f"Точка с координатами ({x};{y}) принадлежит кругу.")
# else:
#     print(f"Точка с координатами ({x};{y}) не принадлежит кругу.")
#
# Задача 5
# Вводятся три целых числа. Определить какое из них наибольшее.
# num_1 = int(input("Введите первое целое число "))
# num_2 = int(input("Введите второе целое число "))
# num_3 = int(input("Введите третье целое число "))
#
# if num_1 > num_2 and num_1 > num_3:
#     print(f"Первое число {num_1} наибольшее")
# elif num_2 > num_1 and num_2 > num_3:
#     print(f"Второе число {num_2} наибольшее")
# else:
#     print(f"Третье число {num_3} наибольшее")
#
# Задача 6
# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# a = int(input("Введите длину первого отрезка: "))
# b = int(input("Введите длину второго отрезка: "))
# c = int(input("Введите длину третьего отрезка: "))
#
# if a + b > c and b + c > a and a + c > b :
#     print("Треугольник существует.")
# else:
#     print("Треугольник не существует.")
#
# if a == b and b == c and a == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний.")

# Задача 7
# Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.
#
# x = int(input("Введите х координату точки: х = "))
# y = int(input("Введите y координату точки: y = "))
# if x == 0 and y == 0:
#     print(f"Точка с координатами ({x};{y}) лежит в центре координатной плоскости")
# elif x == 0 or y == 0:
#     print(f"Точка с координатами ({x};{y}) лежит на координатной оси")
# elif x > 0 and y > 0:
#     print(f"Точка с координатами ({x};{y}) принадлежит 1 четверти координатной плоскости")
# elif x < 0 and y > 0:
#     print(f"Точка с координатами ({x};{y}) принадлежит 2 четверти координатной плоскости")
# elif x < 0 and y < 0:
#     print(f"Точка с координатами ({x};{y}) принадлежит 3 четверти координатной плоскости")
# else:
#     print(f"Точка с координатами ({x};{y}) принадлежит 4 четверти координатной плоскости")
#
# Задача 8
# Вводятся два целых числа. Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть) и частное (в любом случае).
# num_1 = int(input("Введите первое целое число "))
# num_2 = int(input("Введите второе целое число "))
# a = num_1 // num_2
# b = num_1 % num_2
# if num_1 % num_2 == 0:
#     print(f"Первое число {num_1} делится на второе число {num_2}. Частное от деления = {str(a)}")
# else:
#     print(f"Первое число {num_1} не делится без остатка на второе число {num_2}. "
#           f"Частное от деления = {str(a)}, а остаток = {str(b)}" )
#
# Задача 9
# Заданы строковые объекты a,b:
# a = """
#   File "leveleUp.py", line 34
#     tem = 5 if current_temperature >= 5
# SyntaxError: invalid syntax
# """
#
# b = """
# Traceback (most recent call last):
#   File "leveleUp.py", line 18, in <module>
#     print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
# NameError: name 'current_temperature' is not defined
# """
# Если тип ошибки SyntaxError, заменить последнюю строку любим другим сообщением.
#
# if "SyntaxError" in a:
#     print(a.replace("SyntaxError: invalid syntax", "HELLO, WORLD!"))
# else:
#     print(a)
#
# if "SyntaxError" in b:
#     print(b.replace("SyntaxError: invalid syntax", "HELLO, WORLD!"))
# else:
#     print(b)
#
# Задача 10
# Повторить все методы строковых объектов
#
# Метод capitalize() делает первую букву строки заглавной, а остальные строчными.
# print('hello, world! Welcome to Ukraine'.capitalize())
#
# Метод casefold() делает все буквы строчными
# print('hello, world! Welcome to Ukraine'.casefold())
#
# Метод center(40) занимает 40 символов, а в центре располагает заданный str
# print("world".center(40))
#
# Метод count("") позволяет посчитать колличество слов/букв-аргумента в строке с учетом регистра
# print("Pen Pine Apple Apple Pen".count('Pen'))
#
# Метод encode() кодирует строку, если в ней есть буквы, отличные от латиницы
# print('Univerzita Pavla Jozefa Šafárika v Košiciach'.encode())
# print('Объявление'.encode())
#
# Метод endwith('') вернет True, если строковый объект заканчивается указанным в функции символом.
# print("hello, world! Welcome to Ukraine!".endswith('!'))    # True
# print("hello, world! Welcome to Ukraine!".endswith('.'))    # False
#
# Метод expandtabs() действует на строки с табуляцией и помогает задать величину табуляции вручную
# print("he\tllo, wor\tld!".expandtabs(10))
#
# Метод find("") указывает индекс начала слова в строке, указанного в качестве аргумента
# print("Hello, world! Welcome to Ukraine!".find("world"))
#
# Метод format() вернет в строку число с определенным количеством знаков после точки (в этом случае с 4 знаками).
# print("Balance is {money:.4f}".format(money=349.45))
#
# format_map() - ???
#
# Метод .index() опреляет индекс подстроки в строковом объекте
# print("Hello, world! Welcome to Ukraine!".index("world"))
#
# Метод .isalnum() возвращает True, если в строке только буквы и цифры. False - если есть пробел или другие символы
# print("Today is 2022".isalnum())    # False
# print("Today2022".isalnum())    # True
#
# Метод .isalpha() возвращает True, если в строке только буквы. False - если есть цифры, пробел или другие символы
# print("Ukraine".isalpha())  # True
# print("Today is 2022.".isalpha())   # False
# #
# Метод isascii() проверяет, все ли символы в строке являются символами ascii
# print("Ukraine".isascii())  # True
# print("Украина".isascii())  # False
#
# Метод .isdecimal() возвращает True если в строка содержит число в десятичной системе исчисления и в ней есть хотя бы один символ.
# Иначе возвращает False.
# print(''.isdecimal())  # False
# print('0'.isdecimal())  # True
# print('1'.isdecimal())  # True
# print('1000'.isdecimal())  # True
# print('1.1'.isdecimal())  # False
# print('1 000'.isdecimal())  # False
# print('a'.isdecimal())  # False
#
# Метод .isdigit() проверяет, все ли символы в строке являются цифрами
# print("8940359".isdigit())  # True
# print("89403-59".isdigit())  # False
#
# Метод .isidentifier() показывает, является ли строка является ли строка допустимым идентификатором.
# Ранее говорили, что нельзя названия начинать с цифр, символов и т.д.
# print('continue'.isidentifier())  # True
# print('function_name'.isidentifier())  # True
# print('ClassName'.isidentifier())  # True
# print('_'.isidentifier())  # True
# print('number1'.isidentifier())  # True
# print('1st'.isidentifier())  # False
# print('*'.isidentifier())  # False
#
# Проверяет, все ли символы в строке являются строчными
# print("hello, world".islower())    # True
# print("Hello, World".islower())    # False
#
# Проверяет, все ли символы в строке являются цифрами
# print("8940359".isnumeric())    # True
# print("8940-pub-359".isnumeric())    # False
#
# Проверяет, все ли символы в тексте можно напечатать
# print("Hello! Are you #1?".isprintable())    # True
# print("Hello! It's mine".isprintable())    # True
#
# Проверяет, все ли символы в тексте являются пробелами
# print("     ".isspace())    # True
# print("_     ".isspace())    # False
#
# Начинается ли каждое слово с заглавной буквы
# print("Hello, world! Welcome to Ukraine!".istitle())    # False
# print("Hello, World! Welcome To Ukraine!".istitle())    # True
#
# Проверяет, все ли символы в тексте в верхнем регистре
# print("HELLO, WORLD!".isupper())    # True
# print("Hello, world!".isupper())    # False
#
# Соединяет все элементы кортежа или списка со строками в строку, используя @ в качестве разделителя:
# my_list = ["948", "abc", '567']
# print("@".join(my_list))
#
# Возвращает 40-символьную выровненную по левому краю версию слова. Дополнительный текст добавлен для нагладности
# x = "Ukraine".ljust(40)
# print(f"{x} is my home country")
#
# Делает всю строку в нижнем регистре
# print("HELLO, WORLD!".lower())
#
# Убирает все пробелы слева от строки
# print('   hello    world   '.lstrip())
#
# Метод maketrans() возвращает таблицу перевода, которая сопоставляет каждый символ в строке intab с символом в той же
# позиции в строке outab. Затем эта таблица передается функции translate().
#
# print("Hello Sam!".maketrans("A", "C"))
#
# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable))
#
# Метод .partition("") разделяет строку на 3 части и возвращает кортеж:
# 1 - то, что до разделителя-аргумента, 2 - сам аргумент,  3 - то, что после разделителя-аргумента
# print("Hello, world! Welcome to Ukraine".partition("world!"))
# print("Hello, world! Welcome to Ukraine".partition("Hello"))
#
# Метод .replace("","") заменят слова между собой
# print("Hello, world! Welcome to Ukraine".replace("Ukraine" , "France"))
#
# Метод .rfind("") и .rindex() показывает где последнее вхождение подстроки-аргумента в строку
# print("Hello, world! Welcome to world".rfind("world"))
# print("Hello, world! Welcome to world".rindex("world"))
#
# Метод .rjust(40) возвращает 40-символьную выровненную по правому краю версию слова. Дополнительный текст добавлен для нагладности
# x = "Ukraine".rjust(40)
# print(f"My home country is {x}.")
#
# Метод .rpartition("") ищет последнее вхождение слова-аргумента разделяет строку на 3 части и возвращает кортеж:
# 1 - то, что до разделителя-аргумента, 2 - сам аргумент,  3 - то, что после разделителя-аргумента
# print("I could eat bananas all day, bananas are my favorite fruit".rpartition("bananas"))
#
# Метод .rsplit(", ") разделит строку на список, используя запятую, за которой следует пробел в качестве разделителя
# print("hello, world, hello".rsplit(", "))
#
# Метод .rstrip() удаляет все пробелы в конце (справа) строки:
# print('   hello    world   '.rstrip())
#
# Метод .split() разбивает строку на список, где каждое слово является элементом списка.
# По умолчанию строка разбивается по пробелам, но можно указать аргумент и разбить по символу.
# print("Welcome to Ukraine".split())
# print("Welcome@to@Ukraine".split("@"))
#
# Метод .splitlines() разделяет строку на список, где каждая строка является элементом списка
# print("Hello, world! \nWelcome to Ukraine".splitlines())
#
# Метод .startswith(" ") проверяет, начинается ли строка со слова-аргумента
# print("Hello, world! Welcome to Ukraine".startswith("Hello"))   # True
# print("Hello, world! Welcome to Ukraine".startswith("world"))   # False
#
# Метод .strip() удаляет пробелы в начале и в конце строки
# str_obj = '   world! Welcome   '
# print(str_obj.strip())
# print(f"Hello, {str_obj.strip()} to Ukraine!")
#
# Метод .swapcase() делает строчные буквы прописными, а прописные — строчными:
# print("Hello, world! Welcome to Ukraine".swapcase())
#
# Метод .title() делает первую букву в каждом слове строки заглавной
# print("hello, world! welcome to ukraine".title())
#
# Метод .upper() делает все буквы строки заглавными
# print("hello, world! welcome to ukraine".upper())
#
# Метод .zfill(10) заполняет строку нулями в начале, пока ее длина не станет 10 символов
# print("29486".zfill(10))
# print("56".zfill(10))