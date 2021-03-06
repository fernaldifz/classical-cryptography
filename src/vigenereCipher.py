# Vigenere Cipher Standard (26 huruf alfabet)

def generateKeyVige(inputString, inputKey):
    filteredString = filterAlphabet(inputString)
    filteredKey = filterAlphabet(inputKey)
    if len(filteredString) == len(filteredKey):
        return filteredKey
    elif len(filteredString) < len(filteredKey):
        key = ""
        for i in range(len(filteredString)):
            key += filteredKey[i]
        return key
    else:
        key = filteredKey
        for i in range(len(filteredString) - len(filteredKey)):
            key += filteredKey[i % len(filteredKey)]
        return key

def encryptTextVige(inputString, key):
    result = ""
    filteredString = filterAlphabet(inputString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) + ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return result

def decryptTextVige(encryptedString, key):
    result = ""
    filteredString = filterAlphabet(encryptedString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) - ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return result.lower()

def vigenereStandard(inputString, inputKey):
    key = generateKeyVige(inputString, inputKey)
    encryptedString = encryptTextVige(inputString, key)

    saveCipher(encryptedString)

    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextVige(encryptedString, key))

def filterAlphabet(inputString):
    alphabet = ""
    for character in inputString:
        if character.isalpha():
            alphabet += character
    return alphabet

def saveCipher(encryptedString):
    file = open("../save file/VigenereCipher.txt", "w")
    file.write(encryptedString)
    file.close()

def readCipher():
    file = open("../save file/VigenereCipher.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]

def saveKey(generatedKey):
    file = open("../text/VigenereKey.txt", "w",encoding="utf-8")
    file.write(generatedKey)
    file.close()

def readKey():
    file = open("../text/VigenereKey.txt", "r",encoding="utf-8")
    string = file.readlines()
    file.close()

    return string[0]

def saveMemory(cipher):
    file = open("../text/VigenereMemory.txt", "w",encoding="utf-8")
    file.write(cipher)
    file.close()

def readMemory():
    file = open("../text/VigenereMemory.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]

# vigenereStandard("thisplaintext", "sony")