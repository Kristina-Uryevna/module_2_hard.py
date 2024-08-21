import random


def stone():
    numbers = range(3, 21)
    first_stone = random.choice(numbers)
    return first_stone


first_stone = stone()
print('Первый камень: ', first_stone)

n = int(input('Введите число первого камня: ', ))
result = ""
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if n % (i + j) == 0 and j > i:
            result += str(i) + str(j)

if n != first_stone:
    print(('Числа не совпадают, введите правильное число первого камня'))
else:
    print('Второй камень: ', result)
