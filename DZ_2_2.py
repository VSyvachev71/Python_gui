# Задание 2
# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
a = []
count = int(input('Сколько элементов списка Вы хотите добавить: '))
while count > 0:
    a_el = input('Введите значение списка ')
    a.append(a_el)
    count -= 1
print(a)
for i in range(1, len(a), 2):
    a[i-1], a[i] = a[i], a[i-1]
print(a)