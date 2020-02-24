from random import randint as mrz

a = (int(input("Введіть кількість елементів у списку: ")))
b = (int(input("Введіть  значення, яке повинно бути максимальне в списку: ")))

def fun (a,b):
    list = []
    for i in range(a):
        list.append(mrz(0, b))
    return list
print(fun(a,b))

