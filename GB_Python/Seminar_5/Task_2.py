def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)


print(summa(5, 7))