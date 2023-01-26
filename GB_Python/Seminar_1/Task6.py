print("Данная программа проверит билет на 'счастливый' номер")
ticket_num = int(input("Введите шестизначный номер билета: "))
if 99999 < ticket_num < 1000000:
    fist_digits = ticket_num // 1000
    last_digits = ticket_num % 1000
    if fist_digits == last_digits:
        print("Ура! Счастливый билетик!")
    else:
        print("Повезет в другой раз!")
else:
    print("Введен некорректный номер билета!")
