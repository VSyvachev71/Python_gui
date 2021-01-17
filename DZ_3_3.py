# Задание 3
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


a = int(input('Введите число '))
b = int(input('Введите число '))
c = int(input('Введите число '))

def my_func(a, b, c):
    my_func_list = [a, b, c]
    my_func_list.remove(min(my_func_list))
    print(sum(my_func_list))


my_func(a, b, c)