#разбираем копейки на определенные монеты

print("Ваша задача ввести определенное кол-во копеек:")

n = int(input())

if n < 0:
    print("Деньги не могут быть отрицательными!")
else:
    i = n // 100 #рубли
    k = (n % 100) // 10 #гривны
    m = ((n % 100) % 10) // 3 #латынь
    n = n - ( i * 100 ) - ( k * 10 ) - ( m * 3 )
    l = n / ( 1 / 4 )
print( i , k , m , l)
