from numpy import matrix

def generateKeyPlayfair(inputString):
    keyString = cleanKeyAlphabet(inputString)
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    squareKey = [[j for j in range(0,5)] for i in range(0,5)]
    counter = 0

    for character in upperCase:
        if (character not in keyString) and (character not in ["j","J"]):
            keyString += character
    
    for row in range(0,5):
        for col in range(0,5):
            squareKey[row][col] = keyString[counter]
            counter += 1
    
    return squareKey

def encryptTextPFC(inputString):
    pass

def matrixFactory(inputString):
    stringPFC = cleanTextAlphabet(inputString)
    counter = 0

    matrixRow = len(stringPFC) // 2
    matrixPFC = [[j for j in range(0,2)] for i in range(0,matrixRow)]
    
    for row in range(0,matrixRow):
        for col in range(0,2):
            matrixPFC[row][col] = stringPFC[counter]
            counter += 1

    return matrixPFC

def decryptTextPFC(inputString):
    pass

def filterAlphabet(inputString):
    alphabet = ""

    for character in inputString:
        if character.isalpha():
            alphabet += character

    return alphabet.upper()

def cleanKeyAlphabet(inputString):
    cleanAlphabet = ""

    alphabet = filterAlphabet(inputString)

    for character in alphabet:
        if (character not in cleanAlphabet) and (character not in ["j","J"]) :
            cleanAlphabet += character
    
    return cleanAlphabet

def cleanTextAlphabet(inputString):
    cleanAlphabet = ""
    processing = True
    counter = 0
    alphabet = filterAlphabet(inputString)

    # for character in alphabet:
    #     cleanAlphabet += character
        # temuiibu
    while processing:
        for i in range(0,len(alphabet)):
            pass

    if (len(cleanAlphabet) % 2) == 1:
        cleanAlphabet += 'X'

    return cleanAlphabet

