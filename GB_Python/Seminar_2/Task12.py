import random

X = random.randint(0, 1000)
Y = random.randint(0, 1000)
print("Загаданы 2 числа!")
# print(X)
# print(Y)
S = X + Y
print(f"Сумма этих чисел = {S}")
P = X * Y
print(f"Произведение этих чисел = {P}")
z = ((S / 2) ** 2 - P) ** 0.5
print(f"Были загаданы числа: {int( S/2 - z )} и {int( S/2 + z )}")
