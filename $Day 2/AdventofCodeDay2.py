class BagGame:
    def __init__(self, gameNumber, roundList):
        self.gameNumber = gameNumber
        self.roundList = roundList
        self.maxBlue = 0
        self.maxRed =  0
        self.maxGreen = 0

    def getRoundList(self):
        return self.roundList
    def setMaxBlue(self, max):
        self.maxBlue = max

    def setMaxRed(self, max):
        self.maxRed = max

    def setMaxGreen(self, max):
        self.maxGreen = max

    def getMaxBlue(self):
        return self.maxBlue

    def getMaxRed(self):
        return self.maxRed

    def getMaxGreen(self):
        return self.maxGreen

    def getGameID(self):
        return self.gameNumber

class GameRound:
    def __init__(self, blue, red, green):
        self.blue = blue
        self.red = red
        self.green = green

    def getBlue(self):
        return self.blue

    def getRed(self):
        return self.red

    def getGreen(self):
        return self.green

allGames = []
lineWoutN = []

with open("day2input", "r") as gameInfo:
    lines = gameInfo.readlines()

    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

#print(lineWoutN)

for j in lineWoutN:
    roundListInput = []
    colonPlacement = j.find(":")
    gameID = j[5:int(colonPlacement)]
    j = j.split(":")
    j = j[1]
    j = j.split(";")
    for rounds in j:
        blueInput = 0
        redInput = 0
        greenInput = 0
        if rounds.find("blue") != -1:
            blueInput = rounds[rounds.find("blue") - 3:rounds.find("blue") - 1]
        if rounds.find("red") != -1:
            redInput = rounds[rounds.find("red") - 3:rounds.find("red") - 1]
        if rounds.find("green") != -1:
            greenInput = rounds[rounds.find("green") - 3:rounds.find("green") - 1]
        gameRound = GameRound(int(blueInput), int(redInput), int(greenInput))
        roundListInput.append(gameRound)
    bagGame = BagGame(int(gameID), roundListInput)
    allGames.append(bagGame)

for games in allGames:
    blueMax = 0
    redMax = 0
    greenMax = 0
    for rounds in games.getRoundList():
        if(rounds.getBlue() > blueMax):
            blueMax = rounds.getBlue()
        if(rounds.getRed() > redMax):
            redMax = rounds.getRed()
        if(rounds.getGreen() > greenMax):
            greenMax = rounds.getGreen()
    games.setMaxBlue(blueMax)
    games.setMaxRed(redMax)
    games.setMaxGreen(greenMax)

sum = 0
for games in allGames:
    redCubes = 12
    greenCubes = 13
    blueCubes = 14
    if games.getMaxRed() <= redCubes and games.getMaxGreen() <= greenCubes and games.getMaxBlue() <= blueCubes:
        sum = sum + games.getGameID()

print(f"Game sum of the ID's is {sum}")

powerSum = 0
for games in allGames:
    powerSum = powerSum + (games.getMaxBlue()*games.getMaxRed()*games.getMaxGreen())

print(f"Sum of power of the game sets = {powerSum}")
