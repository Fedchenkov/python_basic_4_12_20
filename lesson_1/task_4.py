'''
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

user_number = input("Введите целое число\n>>> ")

if user_number.isdigit():
    user_number = int(user_number)
else:
    print("Ошибка ввода, введите целое число")
    exit()

result = 0
while user_number and result !=9:
    tmp = user_number % 10
    if tmp > result:
        result = tmp
    user_number //=10
print(result)