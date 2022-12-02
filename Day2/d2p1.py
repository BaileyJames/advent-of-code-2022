file = open("./input.txt", "r")

input = file.read()

inputArr = []

inputArr.append(input.split("\n"))

points = 0

print(inputArr[0][0])

for x in inputArr[0]:
    opponent = x[0]
    you = x[2]

    if(opponent == "A"):
        if(you == "Y"):
            points += 8
        if(you == "X"):
            points += 4
        if(you == "Z"):
            points += 3
    elif(opponent == "B"):
        if(you == "Y"):
            points += 5
        if(you == "X"):
            points += 1
        if(you == "Z"):
            points += 9
    elif(opponent == "C"):
        if(you == "Y"):
            points += 2
        if(you == "X"):
            points += 7
        if(you == "Z"):
            points += 6
    

print(points)