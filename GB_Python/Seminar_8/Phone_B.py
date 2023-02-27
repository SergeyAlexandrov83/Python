import sys
import sqlite3


def print_menu():
    print('\nПожалуйста, выберите один из вариантов:')
    print('1. Добавить новый контакт')
    print('2. Отобразить все контакты')
    print('3. Редактировать контакт')
    print('4. Удалить контакт')
    print('5. Найти контакт')
    print('0. Выйти из программы')


def add_contact():
    while True:
        name = input("Введите имя контакта?: ")
        if len(name) != 0:
            break
        else:
            print("Пожалуйста, введите имя:")
    while True:
        surname = input("Введите фамилию контакта?: ")
        if len(surname) != 0:
            break
        else:
            print("Пожалуйста, введите фамилию:")
    while True:
        num = input("Введите номер телефона? (10 цифр): ")
        if not num.isdigit():
            print("Пожалуйста, вводите только цифры")
            continue
        elif len(num) != 10:
            print("Пожалуйста, введите 10 цифр номера телефона без пробелов, дефисов и прочего")
            continue
        else:
            break
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                   (name, surname, num))
    conn.commit()
    print("Новый контакт " + surname + ' ' + name + " был добавлен в телефонную книгу")


def display_book():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)


def key_pair_reception(string):
    print("\nПожалуйста, выберите поле для " + string + " (от 1 до 3)")
    print('1. Имя')
    print('2. Фамилия')
    print('3. Номер телефона')
    print('0. Вернуться в основное меню')
    n = int(input('Ваш выбор: '))
    if n == 1:
        field = "name"
    elif n == 2:
        field = "surname"
    elif n == 3:
        field = "phone_number"
    else:
        return None
    keyword = input("\nПожалуйста, введите значение ключа: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair


def edit_contacts():
    s = key_pair_reception('searching')
    u = key_pair_reception('updating')
    if s is not None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Запись с " + s + " удалена.\n")


def delete_contacts():
    s = key_pair_reception('searching')
    if s is not None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Запись с " + s + " удалена.\n")


def find_contacts():
    s = key_pair_reception('searching')
    if s is not None:
        sql = 'SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)


# Основная программа
print('\nWELCOME TO THE PHONE DIRECTORY')
conn = sqlite3.connect('my.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text)''')
m = -1
while m != 0:
    print_menu()
    m = int(input('Ваш выбор: '))
    if m == 1:
        add_contact()
        continue
    elif m == 2:
        display_book()
        continue
    elif m == 3:
        edit_contacts()
        continue
    elif m == 4:
        delete_contacts()
        continue
    elif m == 5:
        find_contacts()
        continue
    elif m == 0:
        print('Работы программы завершена.\n')
        conn.close()
        sys.exit(0)
    else:
        print('Пожалуйста. следуйте инструкции')
