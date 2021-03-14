def savings(deposit, percent, time):
    return deposit * (1 + percent / 100) ** time


while 1:
    try:
        print("Введите свой депозит :")
        deposit = int(input())
        print("Введите проценты : ")
        percent = int(input())
        print("Введите срок в месяцах : ")
        time = int(input())
    except ValueError:
        print("Введено не число")
        continue
    else:
        print(f"{savings(deposit, percent, time):.2f}")
        print("Продолжим? y/n")
        answer = input()
        if answer == 'y':
            continue
        else:
            break
