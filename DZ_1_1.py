# Задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
n = 7
b = 'Any'
print(f'Переменная n: {n} а b: {b}')
count = 3
while count > 0:
    n = input('Введите число: ')
    b = input('Введите строку: ')
    print(f'Переменная n: {n} а b: {b}')
    count -= 1