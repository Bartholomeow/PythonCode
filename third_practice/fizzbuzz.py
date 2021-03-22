def fizzbuzz(a, b):
    """Fizzbuzz for numbers in range(a, b+1)"""
    for i in range(a, b + 1):
        fizz = 'fizz' if i % 3 == 0 else ''
        buzz = 'buzz' if i % 5 == 0 else ''
        print(i if (fizz == '' and buzz == '') else f'{fizz}{buzz}')


fizzbuzz(1, 100)
