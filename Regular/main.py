import re
import csv


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts = list(rows)
    return contacts


def fix_names(contacts_list):
    fixed_list = []
    for contact in contacts_list:
        pattern = r'[\s,]'
        full_name = (re.split(pattern, ' '.join(contact[:3])))[:3]
        info = contact[3:]
        contact = full_name + info
        fixed_list.append(contact)
    return fixed_list


def fix_phones(contacts_list):
    fixed_list = []
    for contact in contacts_list:
        pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\-?\s*(\d{3})\-?' \
                  r'(\d{2})\-?(\d+)(\s*)\(*([доб.]*)?\s*(\d{4})?\)*'
        phone_exist = re.search(pattern, contact[-2])
        if phone_exist is not None:
            result = re.sub(pattern, r'+7(\2)\3-\4-\5\6\7\8', contact[-2])
            contact[-2] = result
        fixed_list.append(contact)
    return fixed_list


def fix_doubles(contacts_list):
    to_del = []
    for contact in contacts_list:
        pattern = ', '.join([contact[0], (contact[1])])
        start_slice = contacts_list.index(contact) + 1
        for element in contacts_list[start_slice:]:
            full_name = ', '.join([element[0], (element[1])])
            result = re.search(pattern, full_name)
            if result is not None:
                if contact[2] == '':
                    contact[2] = element[2]
                if contact[3] == '':
                    contact[3] = element[3]
                if contact[4] == '':
                    contact[4] = element[4]
                if contact[5] == '':
                    contact[5] = element[5]
                if contact[6] == '':
                    contact[6] = element[6]
                to_del.append(element)
    fixed_list = [contact for contact in contacts_list if contact not in to_del]
    return fixed_list


def write_to_file(contacts_list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


if __name__ == '__main__':
    address_book = read_file('phonebook_raw.csv')
    address_book = fix_names(address_book)
    address_book = fix_phones(address_book)
    address_book = fix_doubles(address_book)
    write_to_file(address_book)

