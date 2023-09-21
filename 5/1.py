from math import pi, e, log1p, sqrt

a = float(input('Введите a: '))
b = float(input('Введите b: '))

if a > b:
    d = (pi ** 2 * sqrt(a ** 3 - b ** 3)) - ((e ** 0.5 + log1p(a * b)) / (0.5 ** 8))
    print(f'Результат: {d}')
else:
    print('а должно быть больше b, т.к. корень должен быть положительным')
