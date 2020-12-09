'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

revenue = float(input("Введите выручку фирмы: ")) # Такой input в этой задаче чтобы не нагромождать код
costs = float(input("Введите издержки фирмы: "))

if revenue > costs:
    print(f'Фирма отработала с прибылью. Рентабельность {revenue / costs:.2f}')
    workers = int(input("Введите количество сотрудников : "))
    print(f'Выручка на одного сотрудника = {revenue / workers:.2f}')
    print(f'Прибыль на одного сотрудника = {(revenue - costs) / workers:.2f}')
elif revenue == costs:
    print('Фирма самоокупаема, но не приносит прибыли.')
else:
    print('Фирма несёт убытки')