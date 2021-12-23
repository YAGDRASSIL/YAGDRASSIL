# выделяем дробную часть числа

import math

print("Введите ваше число:")

i = float(input())

x = math.modf(i)[0]

print("Дробная часть числа", i , "равнва", x)