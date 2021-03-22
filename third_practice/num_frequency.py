def number_frequency(a, b):
    """Count frequency of digits in numbers in range(a, b + 1)"""
    freq_dict = {}
    for i in range(a, b + 1):
        num = i
        if (num == 0):
            freq_dict[0] = freq_dict.setdefault(0, 0) + 1
            continue
        while num > 0:
            digit = num % 10
            freq_dict[digit] = freq_dict.setdefault(digit, 0) + 1
            num //= 10
    for key in sorted(freq_dict):
        print(f"{key} : {freq_dict[key]}")


number_frequency(5, 15)
