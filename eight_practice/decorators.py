import time
from datetime import datetime
import math


def func_benchmark(func_to_decorate):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func_to_decorate(*args, **kwargs)
        print(f'Time = {time.time() - t}')
        return res
    return wrapper


def func_logger(func_to_decorate):
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        res = func_to_decorate(*args, **kwargs)
        t2 = datetime.now()
        with open('eight_practice/log.txt', 'a') as file:
            file.write(
                f'Start time = {t1}; finish time = {t2}; function = {func_to_decorate.__name__}; arguments = {args, kwargs}\n')
        return res
    return wrapper


def func_counter(func_to_decorate):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func_to_decorate(*args, **kwargs)
        print(f'It is {wrapper.count} time')
        return res
    wrapper.count = 0
    return wrapper


@ func_benchmark
@ func_counter
@ func_logger
def is_prime(n):
    """Returns True if n is prime or False if n isn't prime"""
    if n % 2 == 0:
        return f'{n} is not Prime\n'
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return f'{n} is not Prime\n'
    return f'{n} is Prime\n' if n > 1 else f'{n} is not Prime\n'


print(is_prime(999999000001))
print(is_prime(87178291199))
print(is_prime(1013))
print(is_prime(655360001))
print(is_prime(4398042316799))
print(is_prime(1125899839733759))
