from random import randrange

a = randrange(0, 11)
b = randrange(0, 11)
c = randrange(0, 11)

if a > b:
    print(a, b)
    print("Урааа!!!")
if a < b:
    print(a, b)
    print("Всё плохо!")
if a == b:
    print(a, b)
    print("Теперь эта")
    if (a + b) < c:
        print(a + b, c)
        print("Прекрасно!")
    elif (a + b) > c:
        print(a + b, c)
        print("Очень плохо!")
    elif (a + b) == c:
        print(a + b, c)
        print("Страдания")
