# Задача 1.
# Дано два списка. Создать из них список кортежей list_c = [(1,5), (2,6), (3,7), (4,8)]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
# Метод 1
def func(a, b):
    return a, b
list_c = []
for index_a in range(len(list_a)):
    for index_b in range(len(list_b)):
        if index_b == index_a:
            c = func(list_a[index_a], list_b[index_b])
            list_c.append(c)
print(list_c)

# Метод 2
list_d = [(list_a[index], list_b[index]) for index in range(len(list_a))]
print(list_d)

# Задача 2.
# Дан список ["bar", "baz", "qux", "etc"]. Создать кортеж ("foo", "bar", "baz", "qux", "etc")

list_1 = ["bar", "baz", "qux", "etc"]
list_1.insert(0, 'foo')
tuple_1 = tuple(list_1)
print(tuple_1)

# Задача 3.
# Задано список my_list = (1, 2, 3, 4, 5)
# Получите шестой элемент списка. В случае его отсутствия выдайте сообщение о его отсутствии.
my_list = (1, 2, 3, 4, 5)
try:
    print(my_list[6])
except:
    print("Элемент с таким индексом отсутствует.")
