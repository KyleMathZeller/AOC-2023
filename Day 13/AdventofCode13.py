#open and parse data
with open("input13", "r") as day13InfoA:
    lines = day13InfoA.readlines()
    lavaPattern = []
    for line in lines:
        lavaPattern.append(line.replace("\n", ""))

tempList = []
reflectionValue = 0

def horizontalCompare(inputList):
    # compare lines until line N matches line N-1
    # if line N matches compare N+=1 to N-1-= 1 until index edges
    for num in range(len(inputList) - 1):
        if inputList[num] == inputList[num + 1]:
            position1 = num + 2
            position2 = 2 * num + 1 - position1
            while 0 <= position2 and position1 < len(inputList):
                if inputList[position1] != inputList[position2]:
                    break
                position1 += 1
                position2 -= 1
            else:
                return (num + 1)

def verticalCompare(inputList):
    for num in range(len(inputList[0]) - 1):
        col1 = [x[num] for x in inputList]
        col2 = [x[num + 1] for x in inputList]
        if col1 == col2:
            c1 = num + 2
            c2 = 2 * num + 1 - c1
            while 0 <= c2 and c1 < len(inputList[0]):
                col1 = [x[c1] for x in inputList]
                col2 = [x[c2] for x in inputList]
                if col1 != col2:
                    break
                c1 += 1
                c2 -= 1
            else:
                return num + 1

for count, line in enumerate(lavaPattern):
    if len(line) != 0:
        tempList.append(line)
    if len(line) == 0:
        symLine = horizontalCompare(tempList)
        if type(symLine) == int:
            reflectionValue += (symLine * 100)
        symLine = verticalCompare(tempList)
        if type(symLine) == int:
            reflectionValue += symLine
        tempList.clear()
    if count+1 == len(lavaPattern):
        symLine = horizontalCompare(tempList)
        if type(symLine) == int:
            reflectionValue += (symLine * 100)
        symLine = verticalCompare(tempList)
        if type(symLine) == int:
            reflectionValue += symLine
        tempList.clear()

print(reflectionValue)