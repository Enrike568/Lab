from math import e, cos, pi

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

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

t = ((a ** (-1) + b ** (-2) + c ** (-3)) / (pi * abs(a * b))) 
+ ((e ** c + cos(b)) / (cos(c)))

print(f'Результат: {t}')
