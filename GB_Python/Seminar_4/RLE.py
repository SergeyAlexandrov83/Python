def rle_code(data_string):
    code = ''
    char_before = ''
    count = 1
    for char in data_string:
        if char != char_before:
            if char_before:
                code += str(count) + char_before
            count = 1
            char_before = char
        else:
            count += 1
    else:
        code += str(count) + char_before
        return code


def rle_decode(data_string):
    decode = ''
    count = ''
    for char in data_string:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


data = 'AAAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWccccccnhhhhhhhTTTTTTtttrrrrrRRRRRRRR'
cod = rle_code(data)
print(f'Кодированная строка: {cod}')
dec = rle_decode(cod)
print(f'Декодированная строка: {dec}')
