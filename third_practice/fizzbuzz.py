for i in range(0, 101):
    fizz = 'fizz' if i % 3 == 0 else ''
    buzz = 'buzz' if i % 5 == 0 else ''
    print(i if (fizz == '' and buzz == '') else f'{fizz}{buzz}')