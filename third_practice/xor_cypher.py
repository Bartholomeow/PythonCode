def cypher(text, key):
    """
    Returns text encrypted or decrypted with xor

    Keyword arguments:
    text - input text
    key - encryption key

    Returns:
    result (string) - encrypted or decrypted text with xor
    """
    result = ""
    for i in range(len(text)):
        c = ord(text[i])
        d = ord(key[i % len(key)])
        result = result + chr(c ^ d)
    return result


key = 'abc'


encryptedText = cypher('BOOMBOOMBOOM', key)
print(encryptedText)


decryptedText = cypher(encryptedText, key)
print(decryptedText)
