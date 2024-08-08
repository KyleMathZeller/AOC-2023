with open("day15", "r") as day15Info:
    line = day15Info.readlines()
    hashCodes = []
    tempString = ""
    inputString = line[0]
    for number in range(0, len(inputString)):
        if inputString[number] != "," and number != (len(inputString) - 1):
            tempString += inputString[number]
        elif inputString[number] == ",":
            hashCodes.append(str(tempString))
            tempString = ""
        elif number == (len(inputString) - 1):
            tempString += inputString[number]
            hashCodes.append(str(tempString))
            tempString = ""

print(hashCodes)

def hashAlgorithm(inputString, inputValue):
    currentValue = inputValue
    for number in range(0, len(inputString)):
        currentValue += ord(inputString[number])
        currentValue = currentValue * 17
        currentValue = currentValue % 256
        #print(f"charcter {inputString[number]} => {currentValue}")
    return currentValue

hashResults = 0
for string in hashCodes:
    hashResults += hashAlgorithm(string, 0)
print(f"Part 1's sum is {hashResults}")