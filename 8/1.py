from math import e, sin, cos, pi

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

t = ((a ** (-1) + b ** (-2) + c ** (-3)) / (pi * abs(a * b)))
+ ((e ** c + cos(b)) / (cos(c)))

print(f'Результат: {t}')
