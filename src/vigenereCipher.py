# Vigenere Cipher Standard (26 huruf alfabet)

def generateKeyVige(inputString, inputKey):
    if len(filterAlphabet(inputString)) == len(inputKey):
        return inputKey
    elif len(filterAlphabet(inputString)) < len(inputKey):
        key = ""
        for i in range(len(inputString)):
            key += inputKey[i]
        return key
    else:
        key = inputKey
        for i in range(len(filterAlphabet(inputString)) - len(inputKey)):
            key += inputKey[i % len(inputKey)]
        return key

def encryptTextVige(inputString, key):
    result = ""
    j = 0
    for i in range(len(inputString)):
        if(ord(inputString[i].upper()) >= 65 and ord(inputString[i].upper()) <= 90):
            char = (ord(inputString[i].upper()) + ord(key[j].upper())) % 26
            char += ord('A')
            result += chr(char)
            j += 1
    return (result)

def decryptTextVige(encryptedString, key):
    result = ""
    j = 0
    for i in range(len(encryptedString)):
        if(ord(encryptedString[i].upper()) >= 65 and ord(encryptedString[i].upper()) <= 90):
            char = (ord(encryptedString[i].upper()) - ord(key[j].upper())) % 26
            char += ord('A')
            result += chr(char)
            j += 1
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
    return (alphabet)

#VigenereStandard("halo!!!disana", "LEMON")