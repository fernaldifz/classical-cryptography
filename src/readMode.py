def noSpace(string):
    newString = ""
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in string:
        if char in upperCase: 
            newString += char
    
    return newString

def spaceFive(string):
    newString = ""
    n = 5
    
    split_strings = [string[index : index + n] for index in range(0, len(string), n)]
    
    for string in split_strings:
        newString += string + " "

    return newString

def noSpaceDiff(string):
    newString = ""
    counter = 0
    for index in range(0, len(string)):
        if ((index%5) == counter) and (string[index] == " "):
            counter += 1
            if counter >= 5:
                counter = 0
        else:
            newString += string[index]
    
    return newString

# print(noSpaceDiff("akuci ntrap adamu asdaa asdaa asdaa asdas asdaa"))
# string = noSpace("AKU CINTA PADAMU")
# print(string)
# print(spaceFive(string))