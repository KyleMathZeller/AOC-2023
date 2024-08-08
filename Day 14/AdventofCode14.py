with open("input14", "r") as day14InfoA:
    lines = day14InfoA.readlines()
    rockLayout = []
    tempList = []
    for line in lines:
        for character in line:
            if character != "\n":
                tempList.append(character)
        rockLayout.append(list(tempList))
        tempList.clear()

def tiltUp(rockArray):
    row = 0
    rockMoved = False
    while row < len(rockArray[0]) - 1:
        column = 0
        destinationRow = rockArray[row]
        currentRow = rockArray[row + 1]
        while column < len(destinationRow):
            if currentRow[column] == "O" and destinationRow[column] == ".":
                destinationRow[column] = "O"
                currentRow[column] = "."
                rockMoved = True
            column += 1
        if rockMoved and row != 0:
            rockMoved = False
            row -= 1
        elif not rockMoved or row == 0:
            row += 1
    return rockArray

#Got ahead of myself and did not need this
def tiltDown(rockArray):
    row = (len(rockArray) - 1)
    rockMoved = False
    while row > 0:
        column = 0
        destinationRow = rockArray[row]
        currentRow = rockArray[row - 1]
        while column < len(destinationRow):
            if currentRow[column] == "O" and destinationRow[column] == ".":
                destinationRow[column] = "O"
                currentRow[column] = "."
                rockMoved = True
            column += 1
        if rockMoved and row != len(rockArray) - 1:
            rockMoved = False
            row += 1
        elif not rockMoved or row == len(rockArray) - 1:
            row -= 1
    return rockArray

def findLoad(rockArray):
    loadMax = len(rockArray)
    totalLoad = 0
    for num, line in enumerate(rockArray):
        stonesPerLevel = 0
        for char in line:
            if char == "O":
                stonesPerLevel += 1
        totalLoad += (stonesPerLevel * (loadMax - num))
    return totalLoad

#uptilt works
tiltUp(rockLayout)
#print(*rockLayout, sep="\n")
print(findLoad(rockLayout))
