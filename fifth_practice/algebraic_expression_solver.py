import re
import math
operations = ["*", "/", "+", "-", "^"]

priority = {
    "^": 1,
    "*": 2,
    "/": 2,
    "+": 3,
    "-": 3,
    "(": 4,
    "[": 4
}

brackets = {
    ")": "(",
    "]": "["
}

nonnumbers = ["inf", "nan"]


def is_number(input):
    result = re.fullmatch("\d+([.]?\d+)?", input)
    return True if result else False


def conversion(expression):
    stack = []
    result = []
    splitexpr = expression.split()
    if splitexpr[0] == "-":
        result.append("0")
    i = 0
    for item in splitexpr:
        if is_number(item) or item in nonnumbers:
            result.append(item)
        elif item in brackets.values():
            stack.append(item)
        elif item in brackets.keys():
            while stack[-1] != brackets.get(item):
                result.append(stack.pop())
            stack.pop()
        elif item in operations:
            while len(stack) > 0:
                if priority[stack[-1]] <= priority[item]:
                    result += stack.pop() + ' '
                else:
                    break
            stack.append(item)
    while len(stack) > 0:
        result.append(stack.pop())
    return result


def brackets_are_correct(expression):
    stack = []
    for symbol in expression:
        if symbol in brackets.values():
            stack.append(symbol)
        elif symbol in brackets.keys():
            if not stack:
                return False
            if brackets[symbol] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def calc(a, b, operation):
    def add(a1, b1):
        return a1 + b1

    def remove(a1, b1):
        return a1 - b1

    def multiply(a1, b1):
        return a1 * b1

    def divide(a1, b1):
        try:
            result = a1 / b1
        except ZeroDivisionError:
            return math.inf
        else:
            return result

    def pow(a1, b1):
        return a1 ** b1
    selector = {
        "+": add,
        "-": remove,
        "*": multiply,
        "/": divide,
        "^": pow
    }
    return selector[operation](a, b)


def solve_expression(expression):
    rpn = conversion(expression)
    stack = []
    if not rpn:
        return "", "Нет операндов"
    i = 0
    for item in rpn:
        if is_number(item) or item in nonnumbers:
            stack.append(float(item))
        elif item in operations:
            try:
                b = stack.pop()
                a = stack.pop()
            except Exception:
                return "", "Вы ввели что-то не так"
            else:
                stack.append(calc(a, b, item))
    try:
        result = stack.pop()
    except Exception:
        return "", "Вы ввели что-то не так"
    else:
        return int(result) if result % 1 == 0 else round(result, 2), "OK"


def normalize(expression):
    result = ""
    i = 0
    if not brackets_are_correct(expression):
        return "", "Скобки расставлены неверно"
    while i < len(expression):
        if expression[i].isspace():
            pass
        elif expression[i].isdigit():
            while i < len(expression):
                if expression[i].isdigit() or expression[i] == ".":
                    result += expression[i]
                    i += 1
                else:
                    break
            result += " "
            i -= 1
        elif expression[i] in operations + list(brackets.keys()) + list(brackets.values()):
            result += expression[i] + " "
        elif expression[i].isalpha():
            temp = ""
            k = 0
            while i < len(expression) and k < 3:
                if expression[i].isalpha():
                    temp += expression[i]
                    i += 1
                    k += 1
                else:
                    return "", "Неизвестные символы"
            if temp == "inf" or temp == "nan":
                result += temp + " "
                i -= 1
            else:
                return "", "Неизвестные символы"
        i += 1
    return result, "OK"


def print_result(expression, result):
    print(f"{expression} = {result}", end="")


print('''Введите математический пример, состоящий из знаков возведения в степень(^),
умножения(*), деления(/), сложения(+), вычитания(-) и круглых скобок, а затем добавляйте 
к результату оператор и желаемый операнд или группу операторов и операндов''')
result = ""
while 1:
    expression = input()
    if expression == '':
        print('Спасибо за использование')
        break
    expression, error = normalize(str(result) + expression)
    if not expression:
        print(error)
        print("Повторите ввод")
        continue
    result, solveerror = solve_expression(expression)
    if not result:
        print(solveerror)
        print("Повторите ввод")
        continue
    print_result(expression, result)
