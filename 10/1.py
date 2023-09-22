from math import e, cos, pi, atan, sin

x = float(input('Введите a: '))
z = float(input('Введите b: '))


y = atan((x + z) / (pi * sin(z))) + ((e ** 4 *x) / (x * z))

print(f'Результат: {y}')
