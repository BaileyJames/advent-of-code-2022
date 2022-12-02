file = open("./input.txt", "r")

input = file.read()

inputArr = []

inputArr.append(input.split("\n"))

points = 0


for x in inputArr[0]:
    opponent = x[0]
    you = x[2]

    if(opponent == "A"):
        if(you == "Y"):
            points += 4
        if(you == "X"):
            points += 3
        if(you == "Z"):
            points += 8
    elif(opponent == "B"):
        if(you == "Y"):
            points += 5
        if(you == "X"):
            points += 1
        if(you == "Z"):
            points += 9
    elif(opponent == "C"):
        if(you == "Y"):
            points += 6
        if(you == "X"):
            points += 2
        if(you == "Z"):
            points += 7
    

print(points)