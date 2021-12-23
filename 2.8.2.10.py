#считаем сколько столбов пройдем

print("Введите расстояние до превого стоба:")

i = int(input())

print("Введите растояние между стобами:")

k = int(input())

print("Введите длинну шага:")

o = int(input())

print("Введите кол-во шагов:")

j = int(input())

if i < 0 or k < 0 or o < 0 or j < 0:
    print("Данные не верны.")
else:
    shagi = j * o
    dlina = (shagi - i) // k 

print("За ", j , "шагов вы дошли до", dlina, "столба.")