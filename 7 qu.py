Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = int(input())
res = ''
x = n // 100
if x :
    st = "рублей"
    if (x%100)//10 != 1 and x%10 == 1:
        st = "рубль"
    elif (x%100)//10 != 1 and x%10 in [2,3,4] :
        st = "рубля"
    res += str(x) + ' ' + st
y = (n % 100) // 10
if y :
    st = "гривен"
    if (y%100)//10 != 1 and y%10 == 1:
        st = "гривна"
    elif (y%100)//10 != 1 and y%10 in [2,3,4] :
        st = "гривны"
    res += ' + ' + str(y) + ' ' + st 
z = ((n % 100) % 10) // 3
if z :
    st = "алтын"
    if (z%100)//10 != 1 and z%10 in [2,3,4] :
        st = "алтына"
    res += ' + ' + str(z) + ' ' + st
v = (((n % 100) % 10) % 3) * 4
if v :
    st = "полушек"
    if (v%100)//10 != 1 and v%10 == 1:
        st = "полушка"
    elif (v%100)//10 != 1 and v%10 in [2,3,4] :
        st = "полушки"
    res += ' + ' + str(v) + ' ' + st
print(res)
