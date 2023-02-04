import random

n = int(input("Введите количество монеток: "))
coins = []
turn = 0
for i in range(n):
    coins.append(random.randint(0, 1))
    if coins[i] == 1:
        turn += 1
print(coins)
print(turn if turn < n / 2 else n - turn)
