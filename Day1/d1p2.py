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

totalCalories.append(sum(addNums))

highestCals = []

for x in range(3):
    highestCals.append(max(totalCalories))

    totalCalories.remove(max(totalCalories))

print("total", sum(highestCals))