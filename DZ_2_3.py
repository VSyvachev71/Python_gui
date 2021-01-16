# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
               9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
number = int(input('Введите номер месяца: '))
if (number >= 1 and number <= 2) or number == 12:
    print(season_dict[number], season_list[0])
elif number >= 3 and number <= 5:
    print(season_dict[number], season_list[1])
elif number >= 6 and number <= 8:
    print(season_dict[number], season_list[2])
elif number >= 9 and number <= 11:
    print(season_dict[number], season_list[3])
else:
    print('Ввели ошибочное значение')