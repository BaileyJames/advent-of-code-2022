file = open("./input.txt", "r").read().split("\n\n");

crates = file[0]

instructions = file[1]

linesOfCrates = crates.splitlines()

linesOfCrates.pop(-1)

def parseCrates(linesOfCrates):
    
    sortedCrates = [[] for i in range(len(linesOfCrates) + 1)] 

    for x in range(len(linesOfCrates)):

        crate = linesOfCrates[x]

        for i in range(len(crate)):

            if(crate[i] != " " and crate[i] != "" and crate[i] != "[" and crate[i] != "]"):
                if(i == 1): sortedCrates[0].append(crate[i])
                if(i == 5): sortedCrates[1].append(crate[i])
                if(i == 9): sortedCrates[2].append(crate[i])
                if(i == 13): sortedCrates[3].append(crate[i])
                if(i == 17): sortedCrates[4].append(crate[i])
                if(i == 21): sortedCrates[5].append(crate[i])
                if(i == 25): sortedCrates[6].append(crate[i])
                if(i == 29): sortedCrates[7].append(crate[i])
                if(i == 33): sortedCrates[8].append(crate[i])
                if(i == 37): sortedCrates[9].append(crate[i])

    return sortedCrates

def parseInstructions(instructions: str):

    instructionsAsNums = []

    count = 0
    tempArr = []

    instructionsSplit = instructions.splitlines()

    for x in instructionsSplit:
        x = x.split(" ")

        tempArr.append([x[1], x[3], x[5]])

    instructionsAsNums.append(tempArr)   

    return instructionsAsNums

def performInstructions(instructions: list, crates: list):

    newCrates = crates

    finalString = ""

    print("AA", crates)
    for x in range(len(instructions[0])):
        currentInstruction = instructions[0][x]

        print("Ins", currentInstruction)

        for i in range(int(currentInstruction[0])):

            newCrates[int(currentInstruction[2]) -1].insert(0, newCrates[int(currentInstruction[1]) -1][0])

            newCrates[int(currentInstruction[1]) -1].remove(newCrates[int(currentInstruction[1]) -1][0])

        print()
    for x in range(len(newCrates)):
        if(len(newCrates[x]) > 0):
            finalString += str(newCrates[x][0])

    print("Result", finalString)

parsedIntructions = parseInstructions(instructions)

parsedCrates = parseCrates(linesOfCrates)

# run this
performInstructions(parsedIntructions, parsedCrates)