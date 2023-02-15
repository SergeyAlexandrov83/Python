def power(a, b):
    if b == 1:
        return (a)
    if b != 1:
        return a * power(a, b - 1)


num_A = int(input("Введите число: "))
num_B = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(num_A, num_B))
