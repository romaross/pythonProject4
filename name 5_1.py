# Задание 1. массив 3*4, заполнить случайными числами от 1 до 9
# после заполнения вывести на экран те элементы, котороые больше 6
from random import randint
m = 3
n = 4
res_l = []
for i in range(m):
    l = []
    for j in range(n):
        l.append(randint(1,9))
    res_l.append(l)
print(res_l)
for i in range(m):
    for j in range(n):
        if res_l[i][j] > 6:
            print(res_l[i][j], 'i = ', i, ' j = ', j)
