# Вычислить значение логического выражения

print("Введите значение X: ")

x = int(input())

print("Введите значение Y: ")

y = int(input())

print("Введите значение z: ")

z = int(input())

print("Значение 1 логического выражения:", (not(x or not(y) or z)))

print("Значение 2 логического выражения:", (y or (x and not(y) or z)))

print("Значение 3 логического выражения:", (not(not(x)and y or z)))

print("Значение 4 логического выражения:", (not( x or not(y) and z) or z ))

print("Значение 5 логического выражения:", (not(x and not(y) or z) and y ))

print("Значение 6 логического выражения:", (not(not(x) or y and z) or x ))

print("Значение 7 логического выражения:", (not(y or not(x) and z )or z ))

print("Значение 8 логического выражения:", (x and not(not(y) or z) or y ))

print("Значение 9 логического выражения:", (not(x or y and z) or not(x) ))

print("Значение 10 логического выражения:", (not(x and y) and (not(x) or not(z))))
