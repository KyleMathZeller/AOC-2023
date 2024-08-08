with open("day3input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []
    for i in lines:
        lineWoutN.append(i.replace("\n", ""))


lineWoutN = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]


markerPositions = []
numericPositions = []
gearPositions = []

#These strings will be a marker for VALID positions 1 == hit, 0 == nondesirable value .
for line in lineWoutN:
    #string for marker positions
    stringMP = ""
    #string for numeric positions
    stringNP = ""
    #strings for gear positions
    stringGP = ""
    for char in line:
        if char.isdecimal():
            stringMP = stringMP + "0"
            stringNP = stringNP + "1"
            stringGP = stringGP + "0"
        elif char == ".":
            stringMP = stringMP + "0"
            stringNP = stringNP + "0"
            stringGP = stringGP + "0"
        elif char == "*":
            stringMP = stringMP + "1"
            stringNP = stringNP + "0"
            stringGP = stringGP + "1"
        else:
            stringMP = stringMP + "1"
            stringNP = stringNP + "0"
            stringGP = stringGP + "0"
    markerPositions.append(stringMP)
    numericPositions.append(stringNP)
    gearPositions.append(stringGP)

allPartNumbersPos = []
validPartNumbers = []
lineCount = 0

for line in lineWoutN:
    #Current number we are validating
    tempNumber = ""
    #Right side of validation range
    charPos = 0
    for char in line:
        if char.isdecimal() and charPos != (len(line) - 1):
            tempNumber = tempNumber + char
        elif tempNumber != "" or (charPos == (len(line) - 1) and char.isdecimal()):
            if char.isdecimal() and charPos == (len(line) - 1):
                tempNumber = tempNumber + char
            numVerified = False
            #Left side of validation range
            charPosOS = (charPos - (len(tempNumber) +1))
            #This will prevent looking at index[-1] in edge cases
            if charPosOS < 0:
                charPosOS = 0
            #Check above
            #First Line cannot check line index -1
            if lineCount != 0:
                if numVerified == False:
                    validationString = markerPositions[(lineCount - 1)]
                    confirmCount = 0
                    for confirmation in validationString:
                        if int(confirmation) == 1 and charPosOS <= confirmCount and confirmCount <= charPos:
                            validPartNumbers.append(tempNumber)
                            numVerified = True
                            break
                        confirmCount += 1
            #Check Below
            #Last line cannot check index length +1 out of bound
            if lineCount != (len(lineWoutN) - 1):
                if numVerified == False:
                    validationString = markerPositions[(lineCount + 1)]
                    confirmCount = 0
                    for confirmation in validationString:
                        if int(confirmation) == 1 and charPosOS <= confirmCount and confirmCount <= charPos:
                            validPartNumbers.append(tempNumber)
                            numVerified = True
                            break
                        confirmCount += 1
            # Check left and right
            if charPos == (len(line) - 1):
                charPosOS = charPos - len(tempNumber)
            if numVerified == False:
                validationString = markerPositions[lineCount]
                confirmCount = 0
                for confirmation in validationString:
                    if int(confirmation) == 1 and (charPosOS == confirmCount or confirmCount == charPos):
                        validPartNumbers.append(tempNumber)
                        numVerified = True
                        break
                    confirmCount += 1
            tempNumber = ""
        else:
            pass
        charPos += 1
    lineCount += 1

sum = 0
for j in validPartNumbers:
    sum = sum + int(j)


print(gearPositions)
print(f'Part 1 awnser = {sum}')