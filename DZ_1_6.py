# Задание 6
a = int(input('Введите сколько километров пробежал в первый день - '))
b = int(input('Введите сколько необходимо километров пробежать - '))
count = 1
while a <= b:
    print(f'{count}-й день: {a:.2f}')
    count += 1
    a = a * 1.1
    if a >= b:
        break
print(f'Спортсмен достигнет результата на {count}-й день - пробежит не менее {b} км.')