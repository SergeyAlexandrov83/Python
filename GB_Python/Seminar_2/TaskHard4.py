k = int(input("Введите число: "))
fib = [0, 1]
for i in range(k - 1):
    fib.append(fib[i] + fib[i + 1])
while k > 0:
    fib.insert(0, fib[1] - fib[0])
    k -= 1
print(fib)
