# Задача 1
# Проработать встроенные функции множеств: all(), any(), enumerate(), len(), max(), min(), sorted(), sum()

# all()
set_all_true = {1, 3, 4, 5}
print(all(set_all_true))

set_all_false = {0, False, ''}
print(all(set_all_false))

set_one_false = {1, 3, 4, 0}
print(all(set_one_false))

set_one_true = {0, False, 5}
print(all(set_one_true))

set_empty = set()
print(all(set_empty))

print("~" * 100)
# any()
set_all_true = {'True', 'False', 'True'}
print(any(set_all_true))

set_one_true = {1, 3, 4, 0}
print(any(set_one_true))

set_all_false = {0, False, ''}
print(any(set_all_false))

set_one_true = {0, False, 5}
print(any(set_one_true))

set_empty = set()
print(any(set_empty))

print("~" * 100)

# enumerate()
set_languages = {'Python', 'Java', 'JavaScript'}
languages_enumerate = enumerate(set_languages)
print(f"set of languages_enumerate: {set(languages_enumerate)}")

grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)

print(f"Type of enumerateGrocery: {type(enumerateGrocery)}")
print(f"List of enumerateGrocery: {list(enumerateGrocery)}")

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(f"List of enumerateGrocery with another start counter: {list(enumerateGrocery)}")

# enumerate() + loop

grocery = {'bread', 'milk', 'butter'}

for item in enumerate(grocery):
    print(item)

for count, item in enumerate(grocery):
    print(count, item)

# changing the default counter
for count, item in enumerate(grocery, 100):
    print(count, item)

print("~" * 100)

# len()
set_languages = {'Python', 'Java', 'JavaScript'}
print(f"Length of {set_languages} is {len(set_languages)}")

set_empty = set()
print(f"Length of {set_empty} is {len(set_empty)}")
print("~" * 100)

# max()
set_numbers = {9, 34, 11, -4, 27}
print(f"Maximum of {set_numbers} is {max(set_numbers)}")

set_languages = {"Python", "C Programming", "Java", "JavaScript"}
print(f"The largest string in {set_languages} is: {max(set_languages)}")
print("~" * 100)

# min()
set_numbers = {9, 34, 11, -4, 27}
print(f"Minimum of {set_numbers} is {min(set_numbers)}")

set_languages = {"Python", "C Programming", "Java", "JavaScript"}
print(f"The smallest string in {set_languages} is: {min(set_languages)}")
print("~" * 100)

# sorted()
set_numbers = {4, 2, 12, 8}
print(f"Sorted {set_numbers} is {sorted(set_numbers)}")

# sorted with reverse=True
py_set = {'e', 'a', 'u', 'o', 'i'}
print(f"Sorted {py_set} in reverse order: {sorted(py_set, reverse=True)}")


# sorted with key

def take_second(elem):
    return elem[1]


random = {(2, 2), (3, 4), (4, 1), (1, 3)}
sorted_set = sorted(random, key=take_second)
print(f"Sorted set of tuples {random} by second element is {sorted_set}")
print("~" * 100)

# sum()
set_marks = {65, 71, 68, 74, 61}
print(f"Sum of elements in {set_marks} is {sum(set_marks)}")
print(f"1000 and sum of elements in {set_marks} is {sum(set_marks, 1000)}")
print("~" * 100)

# Задача 2
# Даны три множества:
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) выполнить intersection этих множеств
set_intersection = set1.intersection(set2, set3)
print(f"Intersection set of {set1}, {set2} and {set3} is {set_intersection}")

# Задача 3
# Даны три множества:
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) выполнить difference этих множеств
set_dif = set1.difference(set2, set3)
print(f"Difference set of {set1}, {set2} and {set3} is {set_dif}")

# Задача 4
# Даны три множества:
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
# Одним действием (одной строкой) виполнить union этих множеств
set_union = set1.union(set2, set3)
print(f"Union set of {set1}, {set2} and {set3} is {set_union}")

# Задача 5
# Добавить список элементов к заданному множеству
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(f"Set {sampleSet} with element from list {sampleList} is {sampleSet}")

# Задача 6
# Вернуть новый набор идентичных элементов из заданных двух наборов
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
new_set6 = set1.intersection(set2)
print(f"New set of identical elements in {set1} and {set2} is {new_set6}")

# Задача 7
# Вернуть новое множество со всеми элементами из обоих множеств, удалив дубликаты
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
new_set7 = set1.symmetric_difference(set2)
print(f"New set of all elements in {set1}, {set2} without identical elements is {new_set7}")

# Задача 8
# Учитывая два множества Python, обновите первый набор элементами, которые существуют только в первом множетве, но не во втором.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(f"New set1 is updated with elements that only exist in the first set but not in second set: {set1}")

# Задача 9
# Удалите элементы 10, 20, 30 из следующего множества
set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print(f"Set1 without 10, 20 and 30: {set1}")

# Задача 11
# Проверьте, есть ли в двух множествах какие-либо общие элементы. Если да, отобразите общие элементы.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set_intersection = set1.intersection(set2)

if len(set_intersection) > 0:
    print(f"Identical elements of {set1} and {set2} is {set_intersection}")
else:
    print(f"Set {set1} and {set2} have no identical elements")

# Задача 12
# Обновите набор 1, добавив элементы из набора 2
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1.update(set2)
print(f"New set1 with elements of {set2} is {set1}")

# Задача 13
# Удалите элементы из set1, которые не являются общими для set1 и set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.symmetric_difference(set2)
print(f"Non-common elements of {set1} and {set2} is {set3}")
for num in set3:
    if num in set1:
        set1.remove(num)
print(f"Set1 without non-common elements is {set1}")
