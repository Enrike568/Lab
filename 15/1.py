from math import sin, cos, pi

'''
1. Импортируем нужные нам функции из библиотеки math
2. Метод float() возвращает число с плавающей точкой
3. Функция input() позволяет вводить данные пользователем, в нашем случаее с клавиатуры.
4. Функция print() выводит заданное сообщение на экран или другое стандартное устройство вывода.
5. f-строки делают очень простую вещь — они берут значения переменных, 
   которые есть в текущей области видимости, и подставляют их в строку. 
   В самой строке вам лишь нужно указать имя этой переменной в фигурных скобках.
   f'Какой-то текст {переменная} какой-то текст'
'''

x = float(input('Введите x: '))
y = float(input('Введите y: '))

B = ((sin(x) ** 3 + cos(x ** 2) ** 3) / (pi * abs(2 * x * y)))

print(f'Результат: {B}')
