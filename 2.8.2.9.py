#расчитываем расстояние от человека до столба

print("Введите ваше расстояние до первого столба:")

k = int(input())

print("Введите расстояние между столбами:")

l = int(input())

print("Введите нужный вам столб:")

r = int(input())

if k < 0 or l < 0:
    print("Клоун введи корректные данные.")
else:
    n = k + l * r
print("Расстояние до ", l, "столба равно", n, "метров.")