# Меняем певрое слово с последним местами

print("Предложение:«Мы обязательно научимся программировать!».")

i = 'Мы обязательно научимся программировать!'

k = "программировать"

j = 'Мы'

i = i.replace(k , j)

i = i.replace(j , k, 1)

print("\n Со сменой первого слова на последнее: ", i)