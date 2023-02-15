# Калькулятор.
# Решать только через рекурсию!.
# Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# На вход подается строка из операторов / * + - и целых чисел.
# Надо посчитать результат введенного выражения.
#
# Например, на входе:
# 1+9/3*7-4
# на выходе:
# 18

def math_solver(solve: str):
    if solve.isnumeric():
        return int(solve)
    else:
        if "+" in solve:
            temp = solve.split("+")
            return math_solver(temp[0]) + math_solver(temp[1])
        if "-" in solve:
            temp = solve.split("-")
            return math_solver(temp[0]) - math_solver(temp[1])
        if "*" in solve:
            temp = solve.split("*")
            return math_solver(temp[0]) * math_solver(temp[1])
        if "/" in solve:
            temp = solve.split("/")
            return math_solver(temp[0]) / math_solver(temp[1])


string: str = input("Введите выражение: ")
print(math_solver(string))
print(eval(string))
