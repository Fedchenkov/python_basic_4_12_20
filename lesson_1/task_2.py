'''
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''


user_sec = input("Введите количество секунд\n >>> ")

if user_sec.isdigit():
    user_sec = int(user_sec)
else:
    print("Ошибка ввода, введите число")
    exit()

hours = user_sec // 3600
minutes = (user_sec - hours * 3600) // 60
seconds = user_sec - (hours * 3600 + minutes * 60 )
print(f'Время в формате чч:мм:сс - {hours} : {minutes} : {seconds}')