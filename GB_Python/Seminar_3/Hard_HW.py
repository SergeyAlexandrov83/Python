import random


def arr_gen(n):
    numbers_arr = [random.randint(1, 50) for _ in range(n)]
    print(numbers_arr)
    return numbers_arr


def find_next(array, num):
    if num + 1 in array:
        return True
    else:
        return False


def find_max(array):
    max_num = 0
    answer = []
    for j in range(len(array) - 2):
        if array[j + 1] - array[j] > max_num:
            max_num = array[j + 1] - array[j]
            answer = [array[j], array[j + 1]]
    return answer


def main():
    num = int(input("Введите длину последовательности: "))
    arr = arr_gen(num)
    arr_min = min(arr)
    arr_max = max(arr)
    temp_arr = []
    for i in range(arr_min, arr_max):
        if i in arr:
            temp_arr.append(i)
            while find_next(arr, i):
                i += 1
            temp_arr.append(i)
    # print(sorted(arr)) # Для облегчения проверки работоспособности программы
    print(find_max(temp_arr))


if __name__ == '__main__':
    main()
