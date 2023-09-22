from math import e, sin, cos, pi

x = float(input('Введите x: '))
y = float(input('Введите y: '))

A = ((abs(sin(2 * x) ** 2) - abs(cos(3 * y)) ** 4)
      / (pi ** 4 + 3.97)) + ((e ** (-x * y) + 10 * x * y) / (1.34 * y ** 4))

print(f'Результат: {A}')
