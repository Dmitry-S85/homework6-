                                    #РАБОТА СО СЛОВАРЯМИ

#Создана переменная и присвоена ей словарь из нескольких пар ключ-значение
my_dict = {'Dmitry': 1985, 'Andrey': 1990}
print(my_dict)

#Выведено значение по ключу 'Dmitry'
print(my_dict['Dmitry'])

#Выведено одно значение по отсутствующему из словаря
print(my_dict.get('Sergey'))

#Добавлены еще две пары ключ-значение
my_dict.update({'Sergey': 1988,
                'Olya': 1987})
print(my_dict)

#ДОРАБОТАЛ с выводом значения из удаленной пары
a = my_dict.pop('Olya')
print(my_dict)
print(a)

                                    #РАБОТА СО МНОЖЕСТВАМИ

#Создана переменную my_set с присвоенным множеством, состоящее из разных типов данных с повторяющимися значениями
my_set = {3, 2.5, 'Hello', 3, (1, 4, 6), True, 'Hello'}
print(my_set)

#Добавлены 2 элемента во множество my_set:
my_set.add(56)
my_set.add('World')
print(my_set)
