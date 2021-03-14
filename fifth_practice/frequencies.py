def letter_frequency(text):
    freq_dict = {}
    for i in range(0, len(text)):
        freq_dict[text[i]] = freq_dict.setdefault(text[i], 0) + 1
    for key in sorted(freq_dict):
        print(f"{key} : {freq_dict[key]}")


# Так как для каждого рода задачи под понятием "слово" можно понять различные вещи, то и вариантов можно придумать много,
# которые будут подходить для одного случая, но не подходить для другого. Например, если мы разделяем обычный текст, то нам понадобится разделение по точке,
# но если мы будем разбирать какой-либо документ, в котором встречаются емэйлы, и нам надо их выделить, то разделение по точке не подойдёт.
# Поэтому я решил для абстрактной задачи использовать обычное разделение по словам с некоторым набором разделителей.
def word_frequency(text):
    freq_dict = {}
    separators = ['.', ',', '?', '!', ':', ';', '\'', '\"']
    for separator in separators:
        text = text.replace(separator, ' ')
    words = text.split()
    for word in words:
        freq_dict[word] = freq_dict.setdefault(word, 0) + 1
    print(words)
