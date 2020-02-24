from math import sqrt
from random import randint

stu = (str(input("Введіть слово: ")))
z = sqrt(9)
def QA(x,y,z):
    dict = {x:randint(y, z)}
    return dict
print(QA(stu, 1, 100000))