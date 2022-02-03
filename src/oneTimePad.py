# One-time pad (26 huruf alfabet)

import random
import string

def createKeyOTP():
    length = 50000
    key = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    file = open("./text/OTPKey.txt", "w")
    file.write(key)
    file.close()

def getKeyOTP():
    with open('./text/OTPKey.txt', 'r') as file:
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
    return result

def OTP(inputString):
    createKeyOTP()
    key = getKeyOTP()
    encryptedString = encryptTextOTP(inputString, key)

    print("hasil enkripsi: " + encryptedString)
    print("hasil dekripsi: " + decryptTextOTP(encryptedString, key).lower())

    file = open("./text/cipherTextOTP.txt", "w")
    file.write(encryptedString)
    file.close()

def filterAlphabet(inputString):
    alphabet = ""
    for character in inputString:
        if character.isalpha():
            alphabet += character
    return alphabet

OTP("saya senang dan bahagia berkuliah di ITB")