# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. N - кол-во элементов первого множества.
# M - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random

n = (int(input("Введите число N элементов: ")))
m = (int(input("Введите число M элементов: ")))
first_list = []
second_list = []
for i in range(n):
    first_list.append(random.randrange(20))
for i in range(m):
    second_list.append(random.randrange(20))
print(first_list)
print(second_list)
first_list = set(first_list)
second_list = set(second_list)
answer_set = first_list.intersection(second_list)
print(answer_set)
