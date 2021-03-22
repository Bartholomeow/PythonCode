import inputoutput


def xor_encryption(source, destination, key):
    """
    Returns text encrypted or decrypted with xor

    Keyword arguments:
    source - path to file with text to be encrypted
    destination - path to the file where you want to save the result
    key - encryption key
    """
    text = inputoutput.read_from_file(source, "b")
    # text = read_from_file(source)
    key = bytearray(key, 'utf-8')
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    inputoutput.write_to_file(result, destination, "b")


# def write_to_file(data, filename):
#     """
#     Write binary data to file

#     Keyword arguments:
#     data - binary data to be written
#     filename - path to the file where you want to save the result
#     """
#     f = open(filename, 'wb')
#     f.write(data)
#     f.close()


# def read_from_file(filename):
#     """
#     Read binary data from file

#     Keyword arguments:
#     filename - path to the file where you want to save the result

#     Returns:
#     data - binary data from file
#     """
#     f = open(filename, 'rb')
#     data = f.read()
#     f.close()
#     return data


key = 'verystongk'
# Шифрование
xor_encryption('sixth_practice/text.txt', 'sixth_practice/text1.txt', key)
# Расшифрование
xor_encryption('sixth_practice/text1.txt', 'sixth_practice/text2.txt', key)
