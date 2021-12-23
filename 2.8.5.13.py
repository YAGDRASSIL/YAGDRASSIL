# вывводим день недели месяц и время года

print("Введиет номер дня недели:")

x = int(input())

if x < 0 or x > 7:
    print("нет такого дня недели.")

print("Введите номер месяца:")

y = int(input())

if y < 0 or y > 12:
    print("Нет такого месяца.")


if x == 1:
    print("понедеьник.")
elif x ==2:
    print("вторник.")
elif x == 3:
    print("Среда.")
elif x == 4:
    print("Четверг.")
elif x == 5:
    print("Пятница.")
elif x == 6:
    print("Суббота.")
elif x == 7:
    print("Воскресенье")

if y == 1:
    print("Месяц: Январь.")
elif y == 2:
    print("Месяц: Февраль.")
elif y == 3:
    print("Месяц: Март.")
elif y == 4:
    print("Месяц: Апрель.")
elif y == 5:
    print("Месяц: Май.")
elif  y == 6:
    print("Месяц: Июнь.")
elif y == 7:
    print("Месяц: Июль.")
elif y == 8:
    print("Месяц: Август.")
elif y == 9:
    print("Месяц: Сентябрь.")
elif y == 10:
    print("Месяц: Октябрь.")
elif y == 11:
    print("Месяц: Ноябрь.")
elif y == 12:
    print("Месяц: Декабрь.")

if y == 12 or y == 1 or y == 2:
    print("Время года зима.")
elif y == 3 or y == 4 or y == 5:
    print("время года весна.")
elif y == 6 or y == 7 or y == 8:
    print("время года лето.")
elif y == 9 or y == 10 or y == 11:
    print("время года осень.")
