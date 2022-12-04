file = open("./input.txt", "r").read().split();

assignments = []

fullAssignments = []

duplicateAssignment = 0

for x in range(len(file)):
    assignments.append(file[x].split(","))

for x in range(len(assignments)):
    firstElf = str(assignments[x][0]).split("-")
    secondElf = str(assignments[x][1]).split("-")
    
    print(firstElf, secondElf)

    if(int(firstElf[0]) >= int(secondElf[0]) and int(firstElf[1]) <= int(secondElf[1])):
        duplicateAssignment += 1
        
    elif(int(secondElf[0]) >= int(firstElf[0]) and int(secondElf[1]) <= int(firstElf[1])):
        duplicateAssignment += 1

print(duplicateAssignment)