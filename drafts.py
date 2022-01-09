# Задача 9
# Заданы строковые объекты a,b:
a = """
  File "leveleUp.py", line 34
    tem = 5 if current_temperature >= 5
SyntaxError: invalid syntax
"""

b = """
Traceback (most recent call last):
  File "leveleUp.py", line 18, in <module>
    print("current_temperature: ---------", current_temperature, f"Type is: ----- {type(current_temperature)}")
NameError: name 'current_temperature' is not defined
"""
# Если тип ошибки SyntaxError, заменить последнюю строку любим другим сообщением.

# Метод .replace("","") заменят слова между собой
if "SyntaxError" in a:
    print(a.replace("SyntaxError: invalid syntax", "HELLO, WORLD!"))
else:
    print(a)