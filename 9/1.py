from math import e, cos, pi

m = float(input('Введите m: '))
v = float(input('Введите v: '))


f = ((m * v ** (2 + m)) / (3 * pi ** (3 - m)))
+ ((e ** (m + 0.5) + abs(v - 10)) / (cos(m) - 25.8))

print(f'Результат: {f}')
