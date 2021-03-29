import math


def is_prime(n):
    if n % 2 == 0 and n != 2 or n % 1 != 0 or n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while (b):
        (a, b) = (b, a % b)
    return abs(a)


def lcm(a, b):
    try:
        lcm = int(abs(a * b) / gcd(a, b))
    except ZeroDivisionError:
        return "Undefined"
    return abs(lcm)
