from functools import reduce


def factorial(n):
    """Return factorial of n with nonrecursive algorithm and lambda"""
    if n == 0:
        return 1
    else:
        return reduce((lambda x, y: x * y), range(1, n + 1))


while 1:
    try:
        num = int(input('Введите целое неотрицательное число:'))
        if num < 0:
            raise Exception('Введите неотрицательное число')
    except ValueError:
        print("Введено не целое число")
        continue
    except Exception as exc:
        print(exc)
        continue
    else:
        print(factorial(num))
        answer = input('Продолжим? y/n ')
        if answer == 'y':
            continue
        else:
            print('Спасибо за использование')
            break
