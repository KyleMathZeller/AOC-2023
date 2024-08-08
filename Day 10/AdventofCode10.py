with open("day10input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []
    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

row = 0
column = 0
currentChar = chr(0)
oldDirection = chr(0)
mapBlueprint = []
count = 1

for startRow, line in enumerate(lineWoutN):
    newLine = []
    for startColumn, char in enumerate(line):
        if char == "S":
            newLine.append("0")
            column = startColumn
            row = startRow
            currentChar = char
        if char != "S":
            newLine.append(".")
    mapBlueprint.append(newLine)

#Checks position about current char
def UpCheck(inputRow, inputColumn, count, oldDirection):
    if inputRow != 0:
        row = inputRow - 1
        char = lineWoutN[row][inputColumn]
        oldDirection = 'D'
        if char == '|' or char == '7' or char == 'F' :
            mapBlueprint[row][inputColumn] = str(count)
            count += 1
            return row, count, char, oldDirection
        elif char == 'S':
            return row, count, char, oldDirection
        

#Check the position below current character
def DownCheck(inputRow, inputColumn, count, oldDirection):
    if inputRow != len(lineWoutN):
        row = inputRow + 1
        char = lineWoutN[row][inputColumn]
        oldDirection = "U"
        if char == "|" or char == "L" or char == "J":
            mapBlueprint[row][inputColumn] = str(count)
            count += 1
            return row, count, char, oldDirection
        elif char == 'S':
            return row, count, char, oldDirection


#Checks the left side of current character
def LeftCheck(inputRow, inputColumn, count, oldDirection):
    if inputColumn != 0:
        column = inputColumn - 1
        char = lineWoutN[inputRow][column]
        oldDirection = "R"
        if char == "-" or char == "L" or char == "F":
            mapBlueprint[inputRow][column] = str(count)
            count += 1
            return column, count, char, oldDirection
        elif char == 'S':
            return column, count, char, oldDirection


#Checks the right side of current character
def RightCheck(inputRow, inputColumn, count, oldDirection):
    if inputColumn != len(lineWoutN[0]):
        column = inputColumn + 1
        char = lineWoutN[inputRow][column]
        oldDirection = "L"
        if char == "-" or char == "J" or char == "7":
            mapBlueprint[inputRow][column] = str(count)
            count += 1
            return column, count, char, oldDirection
        elif char == 'S':
            return column, count, char, oldDirection
        
column, count, currentChar, oldDirection = RightCheck(row, column, count, oldDirection)
oldDirection = "L"
while currentChar != "S":
    if currentChar == "|":
        if oldDirection == "D":
            row, count, currentChar, oldDirection = UpCheck(row, column, count, oldDirection)
        elif oldDirection == "U":
            row, count, currentChar, oldDirection = DownCheck(row, column, count, oldDirection)
    elif currentChar == "-":
        if oldDirection == "L":
            column, count, currentChar, oldDirection = RightCheck(row, column, count, oldDirection)
        elif oldDirection == "R":
            column, count, currentChar, oldDirection = LeftCheck(row, column, count, oldDirection)
    elif currentChar == "L":
        if oldDirection == "U":
            column, count, currentChar, oldDirection = RightCheck(row, column, count, oldDirection)
        elif oldDirection == "R":
            row, count, currentChar, oldDirection = UpCheck(row, column, count, oldDirection)
    elif currentChar == "J":
        if oldDirection == "U":
            column, count, currentChar, oldDirection = LeftCheck(row, column, count, oldDirection)
        elif oldDirection == "L":
            row, count, currentChar, oldDirection = UpCheck(row, column, count, oldDirection)
    elif currentChar == "7":
        if oldDirection == "D":
            column, count, currentChar, oldDirection = LeftCheck(row, column, count, oldDirection)
        elif oldDirection == "L":
            row, count, currentChar, oldDirection = DownCheck(row, column, count, oldDirection)
    elif currentChar == "F":
        if oldDirection == "D":
            column, count, currentChar, oldDirection = RightCheck(row, column, count, oldDirection)
        elif oldDirection == "R":
            row, count, currentChar, oldDirection = DownCheck(row, column, count, oldDirection)


midPoint = str(count//2)
print(midPoint)


