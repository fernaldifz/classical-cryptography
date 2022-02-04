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

# string = noSpace("AKU CINTA PADAMU")
# print(string)
# print(spaceFive(string))