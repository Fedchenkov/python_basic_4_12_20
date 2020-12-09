'''
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = input('Введите число - ')

if n.isdigit():
    n = int(n)
else:
    print("Ошибка ввода, введите число")
    exit()

tmp = str(n)
tmp_2 = tmp + tmp
tmp_3 = tmp_2 + tmp
total = n + int(tmp_2) + int(tmp_3)
print('Сумма по формуле "n + nn + nnn":', total )

