# Задание 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user = int(input('Введите положительное число: '))
max_n = 0
while user > 0:
    n1 = user % 10
    n2 = (user // 10) % 10
    user = user // 10
    if n1 > n2:
        if max_n <= n1:
            max_n = n1
    elif n1 < n2 or n1 == n2:
        if max_n <= n2:
            max_n = n2
print(max_n)