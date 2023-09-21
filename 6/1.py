from math import sqrt, e, sin, log1p

x = float(input('Введите x: '))
y = float(input('Введите y: '))
z = float(input('Введите z: '))

S = sqrt(x ** y + y ** z + z ** x + ((e ** x + log1p(abs(sin(y)))) / (z ** 4 * 0.87)))

print(f'Результат: {S}')