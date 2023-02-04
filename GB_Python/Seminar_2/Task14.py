N = int(input("Введите N: "))
degree = 0
while 2**degree < N:
    print(2**degree)
    degree += 1
