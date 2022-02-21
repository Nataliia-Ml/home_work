# Задача 1
# Создайте словарь с количеством элементов не менее 5-ти.
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "maxspeed": 150,
  "color": "yellow",
}
print(f"this_dict without changes: {this_dict}")
print(f"id of this_dict before change: {id(this_dict)}")

# Поменяйте местами значения первого и последнего элемент объекта.
this_dict["brand"], this_dict["color"] = this_dict["color"], this_dict["brand"]
print(f"this_dict after changes: {this_dict}")

# Удалите второй элемент.
this_dict.pop("model")
print(f"this_dict after removing the second element: {this_dict}")

# Добавьте в конец ключ «new_key» со значением «new_value».
this_dict["new_key"] = "new_value"

# Выведите на печать итоговый словарь.
print(f"this_dict after adding new element: {this_dict}")

# Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
print(f"id of this_dict after changes: {id(this_dict)}")


# Задача 2
# Как получить значение по ключу "marks" словаря student = {"name": "Emma", "class": 9, "marks": 75}
student = {"name": "Emma", "class": 9, "marks": 75}
print(f"values of keys 'marks' is {student['marks']}")

# Задача 3
# Что выведет этот код?
p = {"name": "Mike", "salary": 8000}
print(p.get("age"))
# Вернет None, так как ключ "age" отстствует

# Задача 4
# Как получить "d" из списка 'sample'?
sample = {"1": ["a", "b"], "2": ["c", "d"]}
print((sample["2"])[1])

# Задача 5
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Дано
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]

# Получить
# dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]

list_3 = []
for words in list_1:
    list_3.append(words.split("-"))
dict_all = dict(list_3)
print(f"Словарь со всеми странами и городами: {dict_all}")

dict_ = {}
for key, value in dict_all.items():
    if value in list_2:
        dict_[key] = value
print(f"Словарь страна-город для городов из списка list_2: {dict_}")

# Задача 6
# Сгенерировать словарь-шифратор, то есть словарь, где ключ и значение являются символами.
# Используя словарь, зашифровать/расшифровать введенное сообщение.

dict_cipher = {'а': 'б', 'б': 'в', 'в': 'г', 'г': 'д', 'д': 'е', 'е': 'ё', 'ё': 'ж', 'ж': 'з', 'з': 'и', 'и': 'й', 'й': 'к',
               'к': 'л', 'л': 'м', 'м': 'н', 'н': 'о', 'о': 'п', 'п': 'р', 'р': 'с', 'с': 'т', 'т': 'у', 'у': 'ф', 'ф': 'х',
               'х': 'ц', 'ц': 'ч', 'ч': 'ш', 'ш': 'щ', 'щ': 'ъ', 'ъ': 'ы', 'ы': 'ь', 'ь': 'э', 'э': 'ю', 'ю': 'я', 'я': 'а',
               ' ': ' ', ',': ',', '.': '.'}
print("Для шифрования допустимы русские буквы маленького регистра, пробел, точка и запятая.")
message1 = input(str("Введите исходное сообщение: "))
message_cipher1 = ''
for letter in message1:
    new_letter1 = dict_cipher[letter]
    message_cipher1 += new_letter1
print(f"Зашифрованное сообщение: {message_cipher1}")

message_cipher2 = input(str("Введите зашифрованное сообщение: "))
# Для расшифровки я сделала 'реверс' словаря, т.е. ключ стал значением, а значение стало ключом
list_keys = list(dict_cipher.keys())
list_values = list(dict_cipher.values())
dict_uncipher = dict(zip(list_values, list_keys))

message2 = ''
for letter in message_cipher2:
    new_letter2 = dict_uncipher[letter]
    message2 += new_letter2
print(f"Расшифрованное сообщение: {message2}")

# Задача 7
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
new_dict = {num: num**3 for num in range(1, 11)}
print(new_dict)

# Задача 8
# Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
letters = 'qwertyuioppoiuytrewqqqweerttyuuioop'
letter_dict = {}
for letter in letters:
    if letter not in letter_dict:
        letter_dict[letter] = 1
    else:
        letter_dict[letter] = letters.count(letter)
print(letter_dict)


# Задача 9
# Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).

school_dict = {"5a": 27, "5b": 29, "6": 35, "7a": 23, "7b": 20, "7c": 24,
               "8a": 26, "8b": 31, "9a": 23, "9b": 22, "10": 36, "11": 30, }
print(school_dict)
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся,
school_dict['7b'] = 19
print(f"The number of students in 7b has changed. Now in 7b {str(school_dict['7b'])} students.")

# б) в школе появился новый класс,
school_dict['8c'] = 18
print(school_dict)
print(f"New 8c class in our school. There are {str(school_dict['8c'])} students.")

# с) в школе был расформирован (удален) другой класс.
school_dict.pop('7c')
print(f"Class 7с was disbanded in our school. School without this class: {school_dict}")

# Вычислите общее количество учащихся в школе.
list_students_number = sum(list(school_dict.values()))
print(f"The school has {str(list_students_number)} students in total.")

# Задача 10.
# Создайте словарь, где ключами являются числа, а значениями – строки.
# Создайте функционал которий вернет новый словарь, "обратный" исходному,
# т. е. ключами являются строки, а значениями – числа.
old_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", }
print(f"Начальный словарь: {old_dict}")

list_keys = list(old_dict.keys())
list_values = list(old_dict.values())

new_dict = dict(zip(list_values, list_keys))
print(f"Новый словарь, обратный исходному: {new_dict}")
