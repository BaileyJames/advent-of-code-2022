file = open("../input.txt", "r")

data = file.read()

newData = []

newData.append(data.split("\n"))

addNums = []

totalCalories = []

for x in newData[0]:
    if(x == ""):
        totalCalories.append(sum(addNums));
        addNums = []
    else:
        addNums.append(int(x));

highestCal = 0

for x in totalCalories:
    if(x > highestCal):
        highestCal = x

print(highestCal)