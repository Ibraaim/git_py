
'------------------------------Try Except---------------------------'
# Исключения - это обьекты которые прерывают работу кода, елси не были обработаны (связаны с логикой программы)

# print('Hello')
# try:
#     print(15/5)
#     print(12/3)
#     print(5/0)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# print('1234')

#Ошибки - обьекты, которые прерывают работу и их нужно обработать(связаны по большей части с разработчиком)

'''
SyntaxError: unexcepted E0F while parsing
(когда мы не закрыли скобку либо кавычку)

a =
SyntaxError: invalid syntax
(когда мы сделали что-то не правильное в синтаксисе)'''

NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
'''
name_1= 'str'
print(name_2.islower())
NameError: name 'name_2' is not defined'''

IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу
'''list_ = [1,2,3,4,5]
list_[50]
IndexError: list index out of range

[1,2,3].pop(5)
IndexError: pop index out of range
'''

KeyError
# исключение, которое выходит, когда мы обращаемся по несуществующему ключу
'''
dict_ = {'a':1}
dict_['b']
KeyError: 'b'

dict_ = {'a':1}
dict_.get('b') None
'''

ValueError
# исключение, когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных и количество переменных не совпадает с количеством элементов внутри итерируемого обьекта
"""int('10b')
ValueError: invalid literal for int() with base 10: '10b'"""
"""a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)"""

TypeError
# исключение, когда мы пытаемся использовать методы не свойственные какому-то типу данных или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

"""for i in 55:
TypeError: 'int' object is not iterable"""
'''5+'5'
TypeError: unsupported operand type(s) for +: 'int' and 'str' '''

'''{[1,2,3]:'abc'}
TypeError: unhashable type: 'list' '''

'''input('',1)
TypeError: input expected at most 1 argument, got 2'''

AttributeError
# выходит, когда мы обращаемся к несуществующему методу или атрибуту обьекта(типа данных)
'''[].replace('a', '')
AttributeError: 'list' object has no attribute 'replace' '''

IndentationError
# выходит, когда мы не правильно используем отсутпы
"""for i in 5:` `
IndentationError: expected an indented block after 'for' statement on line 80"""
'''        a= 5
        IndentationError: unexpected indent
'''

Exception
# Исключение, которе создали сами, чтобы его вызвать
# raise Exception('Моя ошибка')

'----------------------Вызов исключений-----------------------'
# raise SyntaxError

# import random
# names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
# name = []
# random_nemes = randam.sample(range(len(names)), 3)

# print(random_nemes)

import sys
print(sys.platform)