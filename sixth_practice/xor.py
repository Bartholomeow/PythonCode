def xor_encryption(source, destination, key):
    text = read_from_file(source)
    key = bytearray(key, 'utf-8')
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    write_to_file(result, destination)


def write_to_file(data, filename):
    f = open(filename, 'wb')
    f.write(data)
    f.close()


def read_from_file(filename):
    f = open(filename, 'rb')
    data = f.read()
    f.close()
    return data


key = 'verystongk'
# Шифрование
xor_encryption('sixth_practice/text.txt', 'sixth_practice/text1.txt', key)
# Расшифрование
xor_encryption('sixth_practice/text1.txt', 'sixth_practice/text2.txt', key)
