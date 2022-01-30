# Vigenere Cipher Standard (26 huruf alfabet)

def generateKeyVige(inputString, inputKey):
    filteredString = filterAlphabet(inputString)
    if len(filteredString) == len(inputKey):
        return inputKey
    elif len(filteredString) < len(inputKey):
        key = ""
        for i in range(len(inputString)):
            key += inputKey[i]
        return key
    else:
        key = inputKey
        for i in range(len(filteredString) - len(inputKey)):
            key += inputKey[i % len(inputKey)]
        return key

def encryptTextVige(inputString, key):
    result = ""
    filteredString = filterAlphabet(inputString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) + ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return (result)

def decryptTextVige(encryptedString, key):
    result = ""
    filteredString = filterAlphabet(encryptedString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) - ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return (result)

def VigenereStandard(inputString, inputKey):
    key = generateKeyVige(inputString, inputKey)
    encryptedString = encryptTextVige(inputString, key)

    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextVige(encryptedString, key))

def filterAlphabet(inputString):
    alphabet = ""
    for character in inputString:
        if character.isalpha():
            alphabet += character
    return alphabet

VigenereStandard("halo!!!disana", "LEMON")