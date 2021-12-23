# вычисление возраста 

print("Введите свой возраст:")

k = 1

x =int(input()) 

while x < 0 or x > 120:
    k +=1
    x = int(input("Введиет заново: "))
    print(k)
    if k == 5:
        break
if k == 5:
    print("Ошибка! Это программа для людей!")
else:
    if x > 0 and x <= 7:
        print("Вам в детский сад")
    elif x >= 7 and x <= 18:
            print("Вам в школу")
    elif x >= 18 and x <= 25:
        print("Вам в профессиональное учебное заведение")
    elif x >= 25 and x <= 60:
            print("Вам наа работу")
    elif x >= 60 and x <= 120:
        print("Вам предоставляеться выбор")
  
          
        
