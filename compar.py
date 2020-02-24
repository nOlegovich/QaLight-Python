from random import randint

a = int(input("Максимальна довжина першого списка: "))
b = int(input("Максимальне значення першого списка: "))
c = int(input("Максимальна довжина другого списка: "))
d = int(input("Максимальне значення другого списка: "))

def comp (x,y,z,l):
    firstList = []
    for i in range(x):
        firstList.append(randint(0, y))

        secondList = []
    for i in range(z):
        secondList.append(randint(0, l))

    thirdList = []
    for i in firstList:
        if i in secondList:
            thirdList.append(i)

    if len(thirdList) == 0:
        print("Співпадінь немає!!!")
    else:
        return list(thirdList)

print(comp(a,b,c,d))