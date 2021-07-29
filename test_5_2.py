# Задание 2. Дан список чисел. Посчитать сколько раз
# встречается каждое число. Использовать
# функцию для подсчета числа повторений.
# def number_count(number_list, number)
# Подсказка: для хранения данных
# использовать словарь.
from random import randint


def number_count(number_list, number):
    return number_list.count(number)


numbers = [randint(1, 9) for i in range(20)]
new_dict = {}

for num in set(numbers):
    new_dict[num] = number_count(numbers, num)
print(new_dict)
