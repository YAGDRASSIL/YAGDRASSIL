# решение функций 

import math

print("Введите значение x: ")

x = int(input())

if x > 0:
    y = 1 
elif x == 0:
    y = 0
elif x < 0:
    y = -1

print("Получившееся значение функции: ", y)