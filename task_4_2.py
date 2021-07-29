from random import randint
list1 = []
for i in range(10):
    list1.append(randint(1, 100))
print(list1)

count = 0                        # иницилизация кол-во четных элементов
j = 0                            # инициилизация счетчика цикла
while j < len(list1):            # оператор цикла пока
    if list1[j] % 2 == 0:        # проверка на четность
        count += 1               # подсчет четных элементов
    j += 1                       # увеличение счетчика цикла
print('amount of even numbs in list :', count)
