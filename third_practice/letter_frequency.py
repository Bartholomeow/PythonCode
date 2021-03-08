def letter_frequency(text):
    freq_dict = {}
    for i in range(0, len(text)):
        freq_dict[text[i]] = freq_dict.setdefault(text[i], 0) + 1
    for key in sorted(freq_dict):
        print(f"{key} : {freq_dict[key]}")


letter_frequency('fizzbuzz')