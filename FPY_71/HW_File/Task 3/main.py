# Вероятно здесь много лишнего, но я хотел разобраться в теме получше XD
import os

current = os.getcwd()
folder = 'Files_for_task3'
full_path = os.path.join(current, folder)
files_list = [name for name in os.listdir(full_path) if name.endswith('.txt')]
files_list.sort()
result = {}
length = {}
for file_name in files_list:
    with open(os.path.join(current, folder, file_name), encoding='utf-8') as file:
        file_content = []
        for line in file:
            file_content.append(line)
        result[file_name] = file_content  # Можно и одним словарем обойтись
        length[file_name] = len(file_content)  # Но мне показалось, что так строки 27-29 более читаемы?
with open('result.txt', 'w'):  # Почистим файл перед записью на всякий?
    pass
while length != {}:
    min_len = min(length.values())
    file_name = 0
    for k, v in length.items():
        if v == min_len:
            file_name = k
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(f'{file_name} \n')
        file.write(f'{min_len} \n')
        file.writelines(result[file_name])
        file.write('\n\n')
    del result[file_name]  # Прибираем за собой XD
    del length[file_name]
