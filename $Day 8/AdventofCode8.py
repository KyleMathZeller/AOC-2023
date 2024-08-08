from math import lcm

with open("day8input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))


lineWoutN.remove('')

rlDirections = lineWoutN[0]
nodeMap = {}
nodeList = []
for number, entry in enumerate(lineWoutN):
    if number != 0:
        directionKey = entry.split("=")
        nodeLocation = directionKey[0].replace(" ", "")
        leftRight = directionKey[1].split(",")
        left = leftRight[0].replace(" ", "")
        left = left.replace("(", "")
        right = leftRight[1].replace(" ", "")
        right = right.replace(")", "")
        nodeMap.update({nodeLocation : [left, right]})
        nodeList.append(nodeLocation)

listOfOptions = []
visitedNodes = set()

#Function to count steps until you are at your destination
def StepsToDest(directions, start, end):
    currentNode = start
    count = 0
    while currentNode != end:
        for turn in directions:
            if turn == "L":
                position = 0
            if turn == "R":
                position = 1
            avaliableTurns = nodeMap.get(currentNode)
            count += 1
            currentNode = avaliableTurns[position]
    return count

#Part 1 Solution
#print(StepsToDest(rlDirections, 'AAA', 'ZZZ'))

part2Start = []

for node in nodeList:
    if node[2] == 'A':
        part2Start.append(node)

def Steps2Dest(directions, start):
    currentNode = start
    count = 0
    while currentNode[2] != 'Z':
        print(f'currentNode = {currentNode}')
        for turn in directions:
            if turn == "L":
                position = 0
            if turn == "R":
                position = 1
            avaliableTurns = nodeMap.get(currentNode)
            count += 1
            currentNode = avaliableTurns[position]
    print(f'currentNode = {currentNode}')
    return count

LCM = []

for node in part2Start:
    print(node)
    LCM.append(Steps2Dest(rlDirections, node))

print(lcm(LCM[0], LCM[1], LCM[2], LCM[3], LCM[4], LCM[5]))
