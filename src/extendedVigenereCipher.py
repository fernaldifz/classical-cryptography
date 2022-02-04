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
    file = open("../save file/extendedVigenereCipher.txt", "w",encoding="utf-8")
    file.write(encryptedString)
    file.close()

def readCipher():
    file = open("../save file/extendedVigenereCipher.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]

def saveKey(generatedKey):
    file = open("../text/extendedVigenereKey.txt", "w",encoding="utf-8")
    file.write(generatedKey)
    file.close()

def readKey():
    file = open("../text/extendedVigenereKey.txt", "r",encoding="utf-8")
    string = file.readlines()
    file.close()

    return string[0]

def saveMemory(cipher):
    file = open("../text/extendedVigenereMemory.txt", "w",encoding="utf-8")
    file.write(cipher)
    file.close()

def readMemory():
    file = open("../text/extendedVigenereMemory.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]


def extendedVigenere(inputString, inputKey):
    key = generateKeyExtendedVige(inputString, inputKey)
    encryptedString = encryptTextExtendedVige(inputString, key)

    saveCipher(encryptedString)
    print("key: " + key)
    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextExtendedVige(encryptedString, key))

# extendedVigenere("KEITB??!", "!(+)7")