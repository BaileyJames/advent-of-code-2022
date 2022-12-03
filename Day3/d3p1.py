file = open("./input.txt", "r");

input = file.read();

input = input.split()

newInput = []

duplicateLetters = []

sumOfLetterValues = 0

count = 0

def charToNum(char):
    if(char.islower()):
        return ord(char) - 96
    else:
        return ord(char) - 38

for x in input:
    #Splits each string in half and adds each half to a tuple
    newInput.append([x[0: int(len(x) / 2)], x[-int(len(x) / 2):]])
    count += 1

for x in newInput:
    firstSection = x[0]
    secondSection = x[1]

    for i in firstSection:
        if(i in secondSection):
            duplicateLetters.append(i)
            break

print("Duplicated letters: " , duplicateLetters)

for x in duplicateLetters:
    sumOfLetterValues += charToNum(x)

print("Result: ", sumOfLetterValues)