import ast

with open("day7input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

#lineWoutN = ['32T3K 765', 'T55J5 684', 'KK677 28', 'KTJJT 220', 'QQQJA 483']

'''
#for part 1 use this function instead
def CardValue(card):
    if card.isdecimal():
        return hex(int(card))
    elif card == 'T':
        return hex(10)
    elif card == 'J':
        return hex(11)
    elif card == 'Q':
        return hex(12)
    elif card == 'K':
        return hex(13)
    elif card == 'A':
        return hex(14)

#for part 1 use this code
def CamelScore(hand):
    cardOccurance = []
    for card in hand:
        cardOccurance.append(hand.count(card))
    cardOccurance.sort(reverse=True)
    if cardOccurance[0] == 5:
        matchValue = hex(7)
    elif cardOccurance[0] == 4:
        matchValue = hex(6)
    elif cardOccurance[0] == 3 and cardOccurance[3] == 2:
        matchValue = hex(5)
    elif cardOccurance[0] == 3:
        matchValue = hex(4)
    elif cardOccurance[0] == 2 and cardOccurance[2] == 2:
        matchValue = hex(3)
    elif cardOccurance[0] == 2:
        matchValue = hex(2)
    elif cardOccurance[0] == 1:
        matchValue = hex(1)
    return matchValue
'''

#for part 2 use this one
def CardValue(card):
    if card.isdecimal():
        return hex(int(card))
    elif card == 'T':
        return hex(10)
    elif card == 'J':
        return hex(1)
    elif card == 'Q':
        return hex(12)
    elif card == 'K':
        return hex(13)
    elif card == 'A':
        return hex(14)

#for part 2 use this code
def CamelScore(hand):
    cardOccurance = []
    jokers = 0
    for card in hand:
        if ast.literal_eval(card) == 1:
            jokers += 1
        cardOccurance.append(hand.count(card))
    cardOccurance.sort(reverse=True)
    if cardOccurance[0] == 5 or (cardOccurance[0] == 4 and jokers == 1) or (cardOccurance[0] == 3 and jokers == 2) or (jokers == 3 and cardOccurance[3] == 2) or (jokers == 4):
        matchValue = hex(7)
    elif cardOccurance[0] == 4 or (cardOccurance[0] == 3 and jokers == 1) or (jokers == 2 and cardOccurance[2] == 2) or (jokers == 3):
        matchValue = hex(6)
    elif (cardOccurance[0] == 3 and cardOccurance[3] == 2) or (cardOccurance[0] == 2 and cardOccurance[2] == 2 and jokers == 1):
        matchValue = hex(5)
    elif (cardOccurance[0] == 3) or (cardOccurance[0] == 2 and jokers == 1) or (jokers == 2):
        matchValue = hex(4)
    elif (cardOccurance[0] == 2 and cardOccurance[2] == 2):
        matchValue = hex(3)
    elif (cardOccurance[0] == 2) or (jokers == 1):
        matchValue = hex(2)
    elif cardOccurance[0] == 1:
        matchValue = hex(1)
    return matchValue

def HandValue(inputString):
    splitInput = inputString.split(" ")
    hand = splitInput[0]
    bid = splitInput[1]
    bid = int(bid)
    card1, card2, card3, card4, card5 = hand[0], hand[1], hand[2], hand[3], hand[4]
    card1 = CardValue(card1)
    card2 = CardValue(card2)
    card3 = CardValue(card3)
    card4 = CardValue(card4)
    card5 = CardValue(card5)
    hand = [card1, card2, card3, card4, card5]
    camelScore = CamelScore(hand)
    hand = [camelScore, card1, card2, card3, card4, card5, bid]
    return hand

orderedData = []
for hands in lineWoutN:
    scoredHand = HandValue(hands)
    orderedData.append(scoredHand)
orderedData.sort()

winnings = 0
for placement, values in enumerate(orderedData, start=1):
    handWinning = placement * (values[6])
    winnings += handWinning

print(f'Total winnings are {winnings}')

