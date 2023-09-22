from math import cos, sin, pi, atan

y = float(input('Введите y: '))
z = float(input('Введите z: '))

x = (((sin(y) ** 2 + cos(z) ** 2) / (pi * abs(z * 3 * y))) + (atan(z)))

print(f'Результат: {x}')
