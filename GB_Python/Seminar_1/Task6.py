print("Данная программа проверит билет на 'счастливый' номер")
ticket_num = int(input("Введите шестизначный номер билета: "))
if 99999 < ticket_num < 1000000:
    fist_digits = ticket_num // 1000
    fist_digits_sum = fist_digits % 10 + fist_digits // 10 % 10 + fist_digits // 100 % 10
    last_digits = ticket_num % 1000
    last_digits_sum = last_digits % 10 + last_digits // 10 % 10 + last_digits // 100 % 10
    if fist_digits_sum == last_digits_sum:
        print("Ура! Счастливый билетик!")
    else:
        print("Повезет в другой раз!")
else:
    print("Введен некорректный номер билета!")
