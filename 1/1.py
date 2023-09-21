from math import pi, cos

x = float(input('Введите x: '))
y = float(input('Введите y: '))

z = (((x ** 0.5 + 5 * y) / pi) + 0.55 ** 3 * cos(x))

print(f'Результат: {z}')
