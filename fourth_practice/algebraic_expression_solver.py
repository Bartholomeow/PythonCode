def conversion(expression):
    stack = []
    result = ''
    priority = {
        '^': 1,
        '*': 2,
        '/': 2,
        '+': 3,
        '-': 3,
        '(': 4
    }
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            while i < len(expression) and expression[i].isdigit():
                result += expression[i]
                i += 1
            result += ' '
            i -= 1
        elif expression[i] == '(':
            stack.append(expression[i])
        elif expression[i] == ')':
            while stack[-1] != '(':
                result += stack.pop() + ' '
            stack.pop()
        elif expression[i] in ['^', '*', '/', '+', '-']:
            while len(stack) > 0:
                a = priority.get(stack[-1])
                b = priority.get(expression[i])
                if a <= b:
                    result += stack.pop() + ' '
                else:
                    break
            stack.append(expression[i])
        i += 1
    while len(stack) > 0:
        result += stack.pop() + ' '
    return result


def solve_expression(expression):
    rpn = conversion(expression)
    stack = []
    i = 0
    while i < len(rpn):
        if rpn[i] == ' ':
            i += 1
            continue
        elif rpn[i].isdigit():
            number = rpn[i]
            while i < len(rpn) - 1 and rpn[i + 1].isdigit():
                number += rpn[i + 1]
                i += 1
            stack.append(int(number))
        elif rpn[i] in ['^', '*', '/', '+', '-']:
            b = stack.pop()
            a = stack.pop()
            if rpn[i] == '^':
                stack.append(a ** b)
            elif rpn[i] == '*':
                stack.append(a * b)
            elif rpn[i] == '/':
                stack.append(a / b)
            elif rpn[i] == '+':
                stack.append(a + b)
            elif rpn[i] == '-':
                stack.append(a - b)
        i += 1
    print(f"{expression} = {stack.pop()}")


# a = '35 + 14 * 2 / (1 - 5)^2'
# b = '(15 + 22) * 4 + 31'
# solve_expression(a)
# solve_expression(b)
print('''Введите математический пример, состоящий из знаков возведения в степень(^),
умножения(*), деления(/), сложения(+), вычитания(-) и круглых скобок. (пока не успел реализовать большее,
проверка на правильность введённого примера тоже пока не реализована)''')
solve_expression(input())
