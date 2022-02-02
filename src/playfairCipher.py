#

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

def encryptTextPFC(stringText, stringKey):
    plainText, key, bigramMemory, jMemory = rulesSameRowsEnc(stringText, stringKey)
    plainText, key, bigramMemory = rulesSameColsEnc(plainText, key, bigramMemory)
    plainText, key, bigramMemory = otherRulesEnc(plainText, key, bigramMemory)

    return plainText, jMemory

def matrixFactory(inputString):
    stringPFC = cleanTextAlphabet(inputString)
    jMemory = []; counter = 0

    matrixRow = len(stringPFC) // 2
    matrixPFC = [[j for j in range(0,2)] for i in range(0,matrixRow)]
    
    for row in range(0,matrixRow):
        for col in range(0,2):
            if stringPFC[counter] == 'J':
                jMemory.append(counter)
                matrixPFC[row][col] = 'I'
            else:
                matrixPFC[row][col] = stringPFC[counter]

            counter += 1

    return matrixPFC, jMemory

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
    alphabet = filterAlphabet(inputString)
    
    if (len(alphabet) % 2) == 0:
        for i in range(0,len(alphabet),2):
            if alphabet[i] == alphabet[i+1]:
                cleanAlphabet += alphabet[i] + 'X' + alphabet[i+1]
            else:
                cleanAlphabet += alphabet[i] + alphabet[i+1]
    else:
        for i in range(0,len(alphabet)+1,2):
            if i == (len(alphabet)-1):
                cleanAlphabet += alphabet[i] 
            elif alphabet[i] == alphabet[i+1]:
                cleanAlphabet += alphabet[i] + 'X' + alphabet[i+1]
            else:
                cleanAlphabet += alphabet[i] + alphabet[i+1]

    if (len(cleanAlphabet) % 2) == 1:
        cleanAlphabet += 'X'

    return cleanAlphabet

def rulesSameRowsEnc(stringText, stringKey):
    key = generateKeyPlayfair(stringKey)
    plainText, jMemory = matrixFactory(stringText)
    bigramMemory = []

    for row in range(0, len(plainText)):
        for col in range(0,1):
            for keyRow in range(0,5):
                # pass
                if (plainText[row][col] in key[keyRow]) and (plainText[row][col+1] in key[keyRow]):
                    plainText[row][col] = key[keyRow][(key[keyRow].index(plainText[row][col])+1)%5]
                    plainText[row][col+1] = key[keyRow][(key[keyRow].index(plainText[row][col+1])+1)%5]
                    bigramMemory.append(row)

    return plainText, key, bigramMemory, jMemory

def rulesSameRowsDec(plainText, key, bigramMemory):
    pass

def rulesSameColsEnc(plainText, key, bigramMemory):
    counter = 0

    while counter != len(key):
        listBank = []

        for keyCol in range(counter,counter+1):
            for keyRow in range(0,5):
                listBank.append(key[keyRow][keyCol])             

        for row in range(0, len(plainText)):
            for col in range(0,1):
                if (plainText[row][col] in listBank) and (plainText[row][col+1] in listBank):
                    plainText[row][col] = listBank[(listBank.index(plainText[row][col])+1)%5]
                    plainText[row][col+1] = listBank[(listBank.index(plainText[row][col+1])+1)%5]
                    bigramMemory.append(row)
        
        counter += 1

    return plainText,key, bigramMemory

def otherRulesEnc(plainText, key, bigramMemory):
    for row in range(0, len(plainText)):
        if row in bigramMemory:
            pass
        else:
            tmpMemory = []
            for col in range(0,2):
                for keyRow in range(0,5):
                    for keyCol in range(0,5):
                        if(plainText[row][col] == key[keyRow][keyCol]):
                            tmpMemory.append(row)
                            tmpMemory.append(col)
                            tmpMemory.append(keyRow)
                            tmpMemory.append(keyCol)
                
                if len(tmpMemory) == 8:
                    plainText[tmpMemory[0]][tmpMemory[1]] = key[tmpMemory[2]][tmpMemory[7]]
                    plainText[tmpMemory[4]][tmpMemory[5]] = key[tmpMemory[6]][tmpMemory[3]]

    return plainText, key, bigramMemory

def toCipherText(plainTextPFC):
    cipherText = ""

    for row in range(0,len(plainTextPFC)):
        for col in range(0,2):
            cipherText += plainTextPFC[row][col]

    return cipherText

def toFileTXT(cipherText, jMemory):
    file = open("./text/PFCipher.txt", "w")
    file.write(cipherText+'\n')
    for number in jMemory:
        file.write(str(number)+'\n')
    file.close()

def readPFCipherFile():
    file = open("./text/PFCipher.txt", "w")

# print(cleanTextAlphabet("temuiibunantimalamxx"))
# print(encryptTextPFC("temuiibunantimalamjx", "hai"))
p, j = encryptTextPFC("temuiibunantijmajlam", "jalan ganesha sepuluh")
c = toCipherText(p)
toFileTXT(c,j)
