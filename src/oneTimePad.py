import random
import string

def createKeyOTP():
    length = 50000
    key = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    file = open("../text/OTPKey.txt", "w")
    file.write(key)
    file.close()

def getKeyOTP():
    with open('../text/OTPKey.txt', 'r') as file:
        data = file.read().replace('\n', '')
    file.close()
    return data

def encryptTextOTP(inputString, key):
    result = ""
    filteredString = filterAlphabet(inputString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) + ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return result

def decryptTextOTP(encryptedString, key):
    result = ""
    filteredString = filterAlphabet(encryptedString)
    for i in range(len(filteredString)):
        char = (ord(filteredString[i].upper()) - ord(key[i].upper())) % 26
        char += ord('A')
        result += chr(char)
    return result.lower()

def OTP(inputString):
    createKeyOTP()
    key = getKeyOTP()
    encryptedString = encryptTextOTP(inputString, key)

    saveCipher(encryptedString)
    print(key)
    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextOTP(encryptedString, key))

def filterAlphabet(inputString):
    alphabet = ""
    for character in inputString:
        if character.isalpha():
            alphabet += character
    return alphabet

def saveCipher(encryptedString):
    file = open("../save file/OTPCipher.txt", "w")
    file.write(encryptedString)
    file.close()

def readCipher():
    file = open("../save file/OTPCipher.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]

def saveKey(generatedKey):
    file = open("../text/OTPKeys.txt", "w",encoding="utf-8")
    file.write(generatedKey)
    file.close()

def readKey():
    file = open("../text/OTPKeys.txt", "r",encoding="utf-8")
    string = file.readlines()
    file.close()

    return string[0]

def saveMemory(cipher):
    file = open("../text/OTPMemory.txt", "w",encoding="utf-8")
    file.write(cipher)
    file.close()

def readMemory():
    file = open("../text/OTPMemory.txt", "r",encoding="utf-8")
    cipher = file.readlines()
    file.close()

    return cipher[0]


# OTP("aku jauh")