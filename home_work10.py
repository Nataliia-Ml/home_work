# Рассмотреть все методы словаря

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dir(this_dict))
print("this_dict: -----", this_dict, ". Type of this_dict is: -----", type(this_dict))
print(f'ID of this_dict: {id(this_dict)}')
print(f"ID of 'brand' in this_dict: {id(this_dict['brand'])}")
print(f"ID of 'year' in this_dict: {id(this_dict['year'])}")

# copy() - возвращает копию словаря
new_dict = this_dict.copy()
print(f"new_dict is {new_dict}")
print(f"ID of new_dict: {id(new_dict)}")
print(f"ID of 'year' in new_dict: {id(new_dict['year'])}")

# fromkeys(keys, values) - создает словарь. Важно: value должно быть одно, так как это значение будет применено к каждому ключу.
x = ['key1', 'key2', 'key3']
y = 123
new_dict2 = dict.fromkeys(x, y)
print(f"new_dict2: {new_dict2}")

# get(key) - позволяет получить значение по ключу
print(this_dict.get('model'))

# items() - возвращает список тюплов ключ-значение
list_tuples = new_dict2.items()
print(list_tuples)

# keys - возвращает список, содержащий ключи словаря
print(new_dict2.keys())

# pop - Удаляет элемент с указанным ключом
print(f"new_dict: {new_dict}")
new_dict.pop('year')
print(f"new_dict: {new_dict}")

# popitem - Удаляет последнюю вставленную пару ключ-значение
new_dict.popitem()
print(f"new_dict after popitem: {new_dict}")

# setdefault -Возвращает значение указанного ключа. Если ключ не существует: вставьте ключ с указанным значением
x = this_dict.setdefault('model')
print(x)
y = this_dict.setdefault("color", "white")
print(f"this_dict : {this_dict}")

# update - Обновляет словарь указанными парами ключ-значение.
this_dict.update({'speed': 130})
print(f"this_dict after update: {this_dict}")

# values - Возвращает список всех значений в словаре.
list_values = this_dict.values()
print(list_values)

# clear - удаляет все элементы из словаря.
this_dict.clear()
print(f"this_dict after clear: {this_dict}")

