#Code created by Kyle Zeller for Advent of Code 2023 Day 1
with open("input1.txt", "r") as puzzle_codes:
    lines = puzzle_codes.readlines()

    #several extra lists to improve readability
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

    wordsToNumbers = []

    for u in lineWoutN:

        stringToFormat = u

        leftString = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        rightString = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        leftString[0] = stringToFormat.find("one")
        leftString[1] = stringToFormat.find("two")
        leftString[2] = stringToFormat.find("three")
        leftString[3] = stringToFormat.find("four")
        leftString[4] = stringToFormat.find("five")
        leftString[5] = stringToFormat.find("six")
        leftString[6] = stringToFormat.find("seven")
        leftString[7] = stringToFormat.find("eight")
        leftString[8] = stringToFormat.find("nine")

        sumLeftString = sum(leftString)

        if sumLeftString != -9:
            #These are seperate variables to increase readability again
            leftNumberLocation = min(n for n in leftString if n > -1)
            leftNumber = leftString.index(leftNumberLocation) + 1

            rightString[0] = stringToFormat.rfind("one")
            rightString[1] = stringToFormat.rfind("two")
            rightString[2] = stringToFormat.rfind("three")
            rightString[3] = stringToFormat.rfind("four")
            rightString[4] = stringToFormat.rfind("five")
            rightString[5] = stringToFormat.rfind("six")
            rightString[6] = stringToFormat.rfind("seven")
            rightString[7] = stringToFormat.rfind("eight")
            rightString[8] = stringToFormat.rfind("nine")

            rightNumberLocation = max(n for n in rightString if n > -1)
            rightNumber = rightString.index(rightNumberLocation) + 1

            #We only care about the right and left most numbers so therefore also the right and left most words
            if leftNumber == 1:
                stringToFormat = stringToFormat.replace("one", "1")
            elif leftNumber == 2:
                stringToFormat = stringToFormat.replace("two", "2")
            elif leftNumber == 3:
                stringToFormat = stringToFormat.replace("three", "3")
            elif leftNumber == 4:
                stringToFormat = stringToFormat.replace("four", "4")
            elif leftNumber == 5:
                stringToFormat = stringToFormat.replace("five", "5")
            elif leftNumber == 6:
                stringToFormat = stringToFormat.replace("six", "6")
            elif leftNumber == 7:
                stringToFormat = stringToFormat.replace("seven", "7")
            elif leftNumber == 8:
                stringToFormat = stringToFormat.replace("eight", "8")
            elif leftNumber == 9:
                stringToFormat = stringToFormat.replace("nine", "9")
            else:
                pass

            reversedString = ""

            #Reversing the string to ensure the replace hits the right most word
            for w in reversed(stringToFormat):
                reversedString = reversedString + w

            if rightNumber == 1:
                if leftNumber == 2:
                    reversedString = reversedString.replace("en", "1")
                else:
                    reversedString = reversedString.replace("eno", "1")
            elif rightNumber == 2:
                if leftNumber == 8:
                    reversedString = reversedString.replace("ow", "2")
                else:
                    reversedString = reversedString.replace("owt", "2")
            elif rightNumber == 3:
                if leftNumber == 8:
                    reversedString = reversedString.replace("eerh", "3")
                else:
                    reversedString = reversedString.replace("eerht", "3")
            elif rightNumber == 4:
                reversedString = reversedString.replace("ruof", "4")
            elif rightNumber == 5:
                reversedString = reversedString.replace("evif", "5")
            elif rightNumber == 6:
                reversedString = reversedString.replace("xis", "6")
            elif rightNumber == 7:
                reversedString = reversedString.replace("neves", "7")
            elif rightNumber == 8:
                if leftNumber == 1 or 3 or 5 or 9:
                    reversedString = reversedString.replace("thgi", "8")
                else:
                    reversedString = reversedString.replace("thgie", "8")
            elif rightNumber == 9:
                if leftNumber == 7:
                    reversedString = reversedString.replace("eni", "9")
                else:
                    reversedString = reversedString.replace("enin", "9")
            else:
                pass

            forwardString = ""
            #Put the string forwards again
            for x in reversed(reversedString):
                forwardString = forwardString + x

            wordsToNumbers.append(forwardString)
        #if the string has no words to convert to numbers we still need it in our list
        else:
            wordsToNumbers.append(stringToFormat)

    digitsList = []

    #Striping all characters that are not 0-9
    for decodePhrase in wordsToNumbers:
        numberString = "".join(char for char in decodePhrase if char.isdecimal())
        digitsList.append(numberString)

    sum = 0

    for value in digitsList:
        input = value[0] + value [len(value) - 1]
        sum = sum + int(input)

    print(f'Sum = {sum}')