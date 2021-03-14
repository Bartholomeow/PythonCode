def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_lambda_rec(n): return 1 if n == 0 else n * \
    factorial_lambda_rec(n - 1)


while True:
    try:
        num = int(input('Введите число : '))
    except ValueError:
        print('Вы ввели не число')
        continue
    else:
        if(num < 0):
            print('Введите неотрицательное число.')
            continue
        print(f'Факториал числа {num} равен {factorial(num)}')
        print('Продолжим? y/n')
        answer = input()
        if answer == 'y':
            continue
        else:
            break
