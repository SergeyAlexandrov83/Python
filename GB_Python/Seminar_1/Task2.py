print("Данная программа найдет сумму цифр трехзначного числа.")
digit = int(input("Введите трехзначное число: "))
if 99 < digit < 1000:
    digit_sum = digit % 10 + digit // 10 % 10 + digit // 100 % 10
    print(f"Сумма цифр числа {digit} равняется {digit_sum}")
else:
    print("Введено неправильное число!")
