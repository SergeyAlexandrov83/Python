print("Данная программа найдет сумму цифр любого вещественного или целого числа без использования сторонних библиотек")
digit = float(input("Введите число: "))
count = 0
temp = digit
while temp % 1 != 0:
    temp *= 10
    count += 1
if digit < 0:
    digit *= -1  # Или отрицательное надо было считать как -1?
left_part = int(digit // 1)
right_part = digit % 1
digit_sum = 0
while left_part % 10 > 0:
    digit_sum += left_part % 10
    left_part //= 10
while count != 0:
    digit_sum += int(right_part * 10)
    right_part = (right_part * 10) % 1
    count -= 1
print(digit_sum)
