class Documents:
    def __init__(self):
        self.enters = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Иванов"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.bookshelf = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

    def name_by_num(self):  # P
        """ Find Name by doc num """
        number = input('Введите номер документа: ')
        for doc in self.enters:
            if doc["number"] == number:
                return f'Документ с номером {number} принадлежит {doc["name"]}'
        return f'Документ с номером {number} не найден!'

    def shelf_by_num(self):  # S
        """ Find Shelf by doc num """
        number = input('Введите номер документа: ')
        for shelf, value in self.bookshelf.items():
            if number in value:
                return f'Документ с номером {number} находится на полке №{shelf}'
        return f'Документ с номером {number} не найден!'

    def doc_list(self):  # L
        """ Print documents list """
        doc_list = []
        for doc in self.enters:
            doc_list.append(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
        return "\n".join(doc_list)

    def add_doc(self):  # A
        """ Add doc in Documents """
        number = input('Введите номер документа: ')
        doctype = input('Введите тип документа: ')
        name = input('Введите имя: ')
        shelf = input('Введите номер полки для хранения: ')
        if shelf in self.bookshelf.keys():
            new_enter = {"type": doctype, "number": number, "name": name}
            self.enters.append(new_enter)
            self.bookshelf[shelf].append(number)
            return 'Запись успешно добавлена!'
        else:
            return f'Полки с номером {shelf} не существует!'

    def doc_del(self):  # D
        """ Delete doc by doc num """
        number = input('Введите номер документа: ')
        for doc in self.bookshelf.values():
            if number in doc:
                doc.remove(number)
                break
        else:
            return f'Документ с номером {number} не найден!'
        for doc in self.enters:
            if doc["number"] == number:
                self.enters.remove(doc)
                return f'Документ под номером {number} полностью удален!'

    def move_to_shelf(self):  # M
        """ Move doc from shelf to shelf """
        shelf_to_move = input('Введите номер полки для перемещения: ')
        if shelf_to_move not in self.bookshelf.keys():
            return f'Полка с номером {shelf_to_move} не существует!'
        number = input('Введите номер документа: ')
        for saved_doc in self.bookshelf.values():
            if number in saved_doc:
                saved_doc.remove(number)
                self.bookshelf[shelf_to_move].append(number)
                return f'Документа №{number} на полку {shelf_to_move} успешно перемещен!'
        return f'Документ с номером {number} не найден!'

    def add_bookshelf(self):  # AS
        """ Add new shelf """
        new_shelf = input('Введите номер полки для добавления: ')
        if new_shelf in self.bookshelf.keys():
            return f'Полка с номером {new_shelf} уже существует!'
        else:
            self.bookshelf[new_shelf] = []
            return f'Полка под номером {new_shelf} успешно добавлена!'


def main():
    print('Перечень доступных команд - "h"')
    archive = Documents()
    commands = {
        'p': [archive.name_by_num],
        's': [archive.shelf_by_num],
        'l': [archive.doc_list],
        'a': [archive.add_doc],
        'd': [archive.doc_del],
        'm': [archive.move_to_shelf],
        'as': [archive.add_bookshelf]
    }
    while True:
        command = input('Введите команду: ').lower()
        if command in commands:
            print(commands[command][0]())
        elif command == 'h':
            print('"H" или "h" - вывод списка доступных команд')
            print('"P" или "p" - выведет имя человека, которому принадлежит документ')
            print('"S" или "s" - выведет номер полки, на которой находится документ')
            print('"L" или "l" - выведет список всех документов')
            print('"A" или "a" - добавит новый документ в каталог и в перечень полок')
            print('"D" или "d" - удалит полностью документ из каталога и из перечня полок')
            print('"M" или "m" - переместит документ на целевую полку')
            print('"AS" или "as" - добавит новую полку в перечень')
            print('"Q" или "q" - завершает работу программы')
        elif command == 'q':
            print('Всего доброго!')
            break
        else:
            print('Введенная команда не поддерживается!')


main()
