# Задание 3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user = input('Введите число: ')
z = int(user) + int(user + user) + int(user + user + user)
print(f'Сумма n+nn+nnn равна {z}')