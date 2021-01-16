# Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user = int(input('Введите время в секундах: '))
hour = (user % (24 * 3600)) // 3600
if hour < 10:
    hour = '0' + str(hour)
#print(hour)
minutes = (user % 3600) // 60
#print(minutes)
if minutes < 10:
    minutes = '0' + str(minutes)
#print(minutes)
user %= 60
if user < 10:
    user = '0' + str(user)
#print(user)
print(f'{hour}:{minutes}:{user}')