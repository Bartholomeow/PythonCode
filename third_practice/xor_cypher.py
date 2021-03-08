#Для шифрования и дешифрования используется один и тот же метод
def cypher(a, b):
    result = ""
    for i in range(len(a)):
        c = ord(a[i])
        d = ord(b[i % len(b)])
        result = result + chr(c ^ d)
    return result


key = 'abc'

encryptedText = cypher('BOOMBOOMBOOM', key)
print(encryptedText)

decryptedText = cypher(encryptedText, key)
print(decryptedText)