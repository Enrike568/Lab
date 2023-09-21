from math import log1p, sin, pi

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

t = ((log1p(abs(a ** 2 - b ** a - c))) / sin(a) + (16.9 ** 3 / pi))

print(f'Результат: {t}')
