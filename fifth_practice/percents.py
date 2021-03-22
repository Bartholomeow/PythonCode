def savings(deposit, percent, time):
    """
    Return the amount of savings from a certain deposit, percentage after a certain amount of time

    Keyword arguments:
    deposit - deposit by number
    percent - percent by number 
    time - time in months

    Returns:
    result (int) - savings
    """
    result = deposit * (1 + percent / 100) ** time
    return result


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
