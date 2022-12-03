file = open("./input.txt", "r");

input = file.read();

input = input.split()

newInput = []

sumOfLetterValues = 0

def charToNum(char):
    if(char.islower()):
        return ord(char) - 96
    else:
        return ord(char) - 38

for x in range(len(input)):
    # Splits into groups of 3
    if(x % 3 == 0):
        newInput.append([input[x], input[x + 1], input[x + 2]])

for x in range(len(newInput)):

    for i in newInput[x][0]:
        if(i in newInput[x][1] and i in newInput[x][2]):
            print(i)
            sumOfLetterValues += charToNum(i)
            break;

print("Result: ", sumOfLetterValues)