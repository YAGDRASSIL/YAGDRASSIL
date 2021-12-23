# вычисляем взависимости от разницы чисел

print("Введите значение x: ")

x = int(input())

print("Введите значение y: ")

y = int(input())

if x > y:
    c = x - y
    print("разность чисел: ", c)
elif x < y:
    c = x + y
    print("Сумма чисел: ", c)
elif x == y: 
    c = x
    print("Занчение функции: ", c)