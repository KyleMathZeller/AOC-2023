with open("day4input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

#lineWoutN = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

cardWinners = []
cardValues = []
cardWinnersInt = []
cardValuesInt = []

for line in lineWoutN:
    winners = ""
    values = ""
    tempString = ""
    discardString, tempString = line.split(":")
    winners, values = tempString.split("|")
    cardWinners.append(winners)
    cardValues.append(values)

sum = 0
for line in cardWinners:
    winningNumbers = line.split(" ")
    tempString = []
    for section in winningNumbers:
        if section.isdecimal():
            tempString.append(section)
    cardWinnersInt.append(tempString)

for line in cardValues:
    valueNumbers = line.split(" ")
    tempString = []
    for section in valueNumbers:
        if section.isdecimal():
            tempString.append(section)
    cardValuesInt.append(tempString)

pointsTotal = 0
cardCount = 1
cardWPoints = {}
cardsWDuplicates = {}
for i in range(0, len(lineWoutN)):
    winnerList = cardWinnersInt[i]
    valueList = cardValuesInt[i]
    cardPoints = 0
    for winner in winnerList:
        for value in valueList:
            if int(winner) == int(value):
                cardPoints += 1
    if cardPoints != 0:
        pointsTotal = pointsTotal + (2 ** (cardPoints - 1))
        cardWPoints.update({cardCount:(2 ** (cardPoints - 1))})
    if cardPoints == 0:
        cardWPoints.update({cardCount:0})
    cardsWDuplicates.update({cardCount:cardPoints})
    cardCount += 1

task2score = 0
cardCountList = []
for i in range(0, len(lineWoutN)):
    cardCountList.append(1)
cardNumber = 1
for i in range(0, len(lineWoutN)):
    duplicates = cardsWDuplicates.get(cardNumber)
    cardWins = cardWPoints.get(cardNumber)
    end = cardNumber + duplicates
    if end > (len(lineWoutN) + 1):
        end = len(lineWoutN)
    #print(f'cardNumber = {cardNumber} and end = {end}')
    for k in range(1, (cardCountList[i] + 1)):
        #Add in order
        for j in range(cardNumber, end):
            cardCountList[j] = cardCountList[j] + 1
    #print(f'We are on card {cardNumber} which we have {cardCountList[i]} copy of it, and add a copy to cards to these numbers {cardNumber+1}-{end} and duplicate = {duplicates}')
    cardNumber += 1

for i in cardCountList:
    task2score = task2score + i

#print(cardCountList)
#print(cardWPoints)
#print(cardsWDuplicates)
print(f'Task 1 = {pointsTotal} Task 2 = {task2score}')
