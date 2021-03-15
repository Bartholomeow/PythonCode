def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_lambda_rec(n): return 1 if n == 0 else n * \
    factorial_lambda_rec(n - 1)


while True:
    print("""Выберите вариант:
    1. Обычной функцией без рекурсии
    2. Лямбдой с рекурсией
    Чтобы выйти нажмите любую другую кнопку
    """)
    item = input()
    if item not in ['1', '2']:
        break
    try:
        num = int(input('Введите число : '))
    except ValueError:
        print('Вы ввели не число')
        continue
    else:
        if(num < 0):
            print('Введите неотрицательное число.')
            continue
        if item == '1':
            fact = factorial(num)
        elif item == '2':
            fact = factorial_lambda_rec(num)
        print(f'Факториал числа {num} равен {fact}')
        print('Продолжим? y/n')
        answer = input()
        if answer == 'y':
            continue
        else:
            break
