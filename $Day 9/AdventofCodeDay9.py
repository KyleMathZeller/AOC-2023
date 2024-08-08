with open("day9input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

parsedInput = []
for array in lineWoutN:
    tempArray = array.split(" ")
    for number in range(len(tempArray)):
        tempArray[number] = int(tempArray[number])
    parsedInput.append(tempArray)

#This function prevents mirrored values from stopping the loop on accident ex. [-1, 1]
def ABSSum(array):
    sum = 0
    for value in array:
        sum = sum + abs(value)
    return sum

def ArrayPrediction(inputArray):
    newArray = inputArray
    extendedArray = []
    extendedArray.append(newArray)
    value = 0
    while ABSSum(newArray) != 0:
        #This section creates the child array's of the input arrays we need to make predictions
        tempArray = []
        for number, value in enumerate(newArray):
            if number != 0:
                value = newArray[number] - newArray[number - 1]
                tempArray.append(value)
        extendedArray.append(tempArray)
        newArray = tempArray
    #I just reversed the arrays to start with the [0, 0] easier for me to navigate
    revExtendedArray = list(reversed(extendedArray))
    #This section extends the arrays sequentially to get our end prediciton values
    for number in range(len(revExtendedArray)):
        if number == 0:
            revExtendedArray[number].append(0)
        if number != 0:
            baseArray = revExtendedArray[number - 1]
            base = baseArray[len(baseArray) - 1]
            leafArray = revExtendedArray[number]
            leaf = leafArray[len(leafArray) - 1]
            newBase = base + leaf
            revExtendedArray[number].append(newBase)
    solutionArray = revExtendedArray[len(revExtendedArray) - 1]
    backSolution = solutionArray[len(solutionArray) - 1]
    #This section was added on for task 2 it generates the "backwards" extrapolation
    for number in range(len(revExtendedArray)):
        if number == 0:
            revExtendedArray[number].append(0)
        if number != 0:
            baseArray = revExtendedArray[number - 1]
            baseF = baseArray[0]
            leafArray = revExtendedArray[number]
            leafF = leafArray[0]
            newBaseF = leafF - baseF
            revExtendedArray[number].insert(0, newBaseF)
    solutionArray = revExtendedArray[len(revExtendedArray) - 1]
    frontSolution = solutionArray[0]
    return backSolution, frontSolution

totalSum = 0
frontSum = 0
for array in parsedInput:
    value = ArrayPrediction(array)
    totalSum = totalSum + value[0]
    frontSum = frontSum + value[1]
print(totalSum, frontSum)