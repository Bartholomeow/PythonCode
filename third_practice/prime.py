import math


def is_prime(n):
    """Returns True if n is prime or False if n isn't prime"""
    if n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1


def gcd(a, b):
    """
    Returns greatect common divisor of two numbers

    Keyword arguments:
    a - first number
    b - second number

    Returns:
    a (int) - greatest common divisor of a and b
    """
    while (b):
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    """
    Returns lowest common multiple of two numbers

    Keyword arguments:
    a - first number
    b - second number

    Returns:
    lcm (int) - lowest common multiple of a and b
    """
    lcm = int(abs(a * b) / gcd(a, b))
    return lcm


while (1):
    print('Select action:')
    print('1. Number is prime?')
    print('2. Find GCD of numbers')
    print('3. Find LCM of numbers')
    print('Press any other button to exit')
    action = input()
    if action == '1':
        while (1):
            print('Enter the number')
            a = input()
            if a.isdigit():
                num = int(a)
                break
            else:
                print('This is not a number')
        print('Number is prime' if is_prime(num) else 'Number is not prime')
    elif action == '2':
        while (1):
            print('Enter 2 numbers')
            a = input()
            b = input()
            if a.isdigit() and b.isdigit():
                num1 = int(a)
                num2 = int(b)
                break
            else:
                print('These are not numbers')
        print(f'GCD of {num1} and {num2} = {gcd(num1, num2)}')
    elif action == '3':
        while (1):
            print('Enter 2 numbers')
            a = input()
            b = input()
            if a.isdigit() and b.isdigit():
                num1 = int(a)
                num2 = int(b)
                break
            else:
                print('These are not numbers')
        print(f'LCM of {num1} and {num2} = {lcm(num1, num2)}')
    else:
        break
