import random


def stone():
    numbers = range(3, 21)
    first_stone = random.choice(numbers)
    return first_stone


first_stone = stone()
print('Первый камень: ', first_stone)


def password(n):
    result = ""
    for i in first_stone:
        for j in range(i):
            if n % (i + j) == 0:
                result = str(i) + str(j)
                return result

result = password(n)
print('Второй камень: ', result)