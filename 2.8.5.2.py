# решение функции

import math

print("Введите значение x: ")

x = int(input())

if x > 0:
    y = math.sin(x)**2
elif x == 0:
    y = 0
elif x < 0:
    y = 1 + 2 * math.sin(x**2)

print("Значение полученной функции: ", y)