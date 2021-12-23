# решение квадротного уравнения

import math

print("Введите значение a: ")

a = int(input())

print("Введите значение b: ")

b = int(input())

print("Введите значение c: ")

c = int(input())

print("Получилось уравнение:",a,"* x**2 +",b,"* x +",c,"= 0")

d = b**2 - 4 * a * c

if d < 0:
    print("Корней нет так как дикриминант:", d,"< 0")
elif d == 0:
    x = (-b + math.sqrt(d))/ 2 * a
    print("Так как d = 0, то один корень ", x )
elif d > 0:
    x1 = (-1 * b + math.sqrt(d))/ 2 * a 
    x2 = (-1 * b - math.sqrt(d))/ 2 * a
    print("Дискиминант равен:", d)
    print("Первый корень:", x1)
    print("Второй корень:",x2)