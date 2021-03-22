def xor_encryption(source, destination, key):
    """
    Returns text encrypted or decrypted with xor

    Keyword arguments:
    source - path to file with text to be encrypted
    destination - path to the file where you want to save the result
    key - encryption key
    """
    with open(source, 'rb') as f:
        text = f.read()
    key = bytearray(key, 'utf-8')
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ key[i % len(key)])
    with open(destination, 'wb') as f:
        f.write(result)


key = 'verystongk'
# Шифрование
xor_encryption('sixth_practice/text.txt', 'sixth_practice/text1.txt', key)
# Расшифрование
xor_encryption('sixth_practice/text1.txt', 'sixth_practice/text2.txt', key)
