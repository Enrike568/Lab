from math import pi, sqrt, e

x = float(input('Введите x: '))
y = float(input('Введите y: '))

z = ((sqrt(abs(x)) + sqrt(abs(3 * y)) ** 2) / (pi ** 3 * 0.75) - e ** 8)

print(f'Результат: {z}')
