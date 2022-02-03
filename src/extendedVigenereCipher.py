# Extended Vigenere Cipher (256 karakter ASCII)

def generateKeyExtendedVige(inputString, inputKey):
    if len(inputString) == len(inputKey):
        return inputKey
    elif len(inputString) < len(inputKey):
        key = ""
        for i in range(len(inputString)):
            key += inputKey[i]
        return key
    else:
        key = inputKey
        for i in range(len(inputString) - len(inputKey)):
            key += inputKey[i % len(inputKey)]
        return key

def encryptTextExtendedVige(inputString, key):
    result = ""
    for i in range(len(inputString)):
        char = (ord(inputString[i]) + ord(key[i])) % 256
        result += chr(char)
    return result

def decryptTextExtendedVige(encryptedString, key):
    result = ""
    for i in range(len(encryptedString)):
        char = (ord(encryptedString[i]) - ord(key[i])) % 256
        result += chr(char)
    return result

def saveCipher(encryptedString):
    file = open("./text/extendedVigenereCipher.txt", "w")
    file.write(encryptedString)
    file.close()

def extendedVigenere(inputString, inputKey):
    key = generateKeyExtendedVige(inputString, inputKey)
    encryptedString = encryptTextExtendedVige(inputString, key)

    saveCipher(encryptedString)

    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextExtendedVige(encryptedString, key))

# extendedVigenere("KEITB??!", "!(+)7")