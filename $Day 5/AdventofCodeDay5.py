with open("day5input", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []

    for i in lines:
        lineWoutN.append(i)


lineWoutN = ['seeds: 79 14 55 13\n', '\n', 'seed-to-soil map:\n', '50 98 2\n', '52 50 48\n', '\n', 'soil-to-fertilizer map:\n', '0 15 37\n',
             '37 52 2\n', '39 0 15\n', '\n', 'fertilizer-to-water map:\n', '49 53 8\n', '0 11 42\n', '42 0 7\n', '57 7 4\n', '\n',
             'water-to-light map:\n', '88 18 7\n', '18 25 70\n', '\n', 'light-to-temperature map:\n', '45 77 23\n', '81 45 19\n',
             '68 64 13\n', '\n', 'temperature-to-humidity map:\n', '0 69 1\n', '1 0 69\n', '\n', 'humidity-to-location map:\n', '60 56 37\n',
             '56 93 4\n']

#print(lineWoutN)
#Seeds parsing
seedsList = lineWoutN[0].split(" ")
for position, item in enumerate(seedsList):
    if item.find("\n") != -1:
        seedsList[position] = item.replace("\n", "")
while seedsList.count("") > 0:
    seedsList.remove("")
seedsList.remove("seeds:")

def ParseData(dataBlock, listName, mapName):
    listName = listName + "\n"
    count = 0
    for position, item in enumerate(lineWoutN):
        if count == dataBlock and (item != listName) and (item != "\n"):
            dstart, rstart, length = lineWoutN[position].split(" ")
            length = length.replace("\n", "")
            mapName.update({int(rstart): [int(dstart), int(length)]})
        if item == '\n':
            count += 1

def RangeParse(dataBlock, listName, arrayName):
    listName = listName + "\n"
    count = 0
    for position, item in enumerate(lineWoutN):
        if count == dataBlock and (item != listName) and (item != "\n"):
            dstart, rstart, length = lineWoutN[position].split(" ")
            dstart = int(dstart)
            rstart = int(rstart)
            length = int(length.replace("\n", ""))
            tempArry = [[rstart, (rstart+length)], (int(dstart) - int(rstart))]
            arrayName.append(tempArry)
        if item == '\n':
            count += 1

#Map parsing
seedsToSoilMap = {}
soilToFertilizer = {}
fertilizerToWater = {}
waterToLight = {}
lightToTemperature = {}
tempToHumidity = {}
humidityToLoc = {}

ParseData(1, "seed-to-soil map:", seedsToSoilMap)
ParseData(2,"soil-to-fertilizer map:", soilToFertilizer)
ParseData(3, "fertilizer-to-water map:", fertilizerToWater)
ParseData(4, "water-to-light map:", waterToLight)
ParseData(5, "light-to-temperature map:", lightToTemperature)
ParseData(6, "temperature-to-humidity map:", tempToHumidity)
ParseData(7, "humidity-to-location map:", humidityToLoc)

seedRange =[]
for value in range(0, len(seedsList), 2):
    seedRange.append([int(seedsList[value]), int(int(seedsList[value]) + int(seedsList[value + 1]))])

seedsToSoilRange = []
soilToFertRange = []
fertToWaterRange = []
waterToLightRange = []
lightToTempRange = []
tempToHumidityRange = []
humidityToLocRange = []
RangeParse(1, "seed-to-soil map:", seedsToSoilRange)
RangeParse(2, "soil-to-fertilizer map:", soilToFertRange)
RangeParse(3, "fertilizer-to-water map:", fertToWaterRange)
RangeParse(4, "water-to-light map:", waterToLightRange)
RangeParse(5, "light-to-temperature map:", lightToTempRange)
RangeParse(6, "temperature-to-humidity map:", tempToHumidityRange)
RangeParse(7, "humidity-to-location map:", humidityToLocRange)

def MapTranslation(var, dictionary):
    temp = -1
    for start in dictionary:
        tempArr = list(dictionary.get(start))
        value = tempArr[0]
        length = tempArr[1]
        if (start <= var) and (var <= (start + length - 1)):
            temp = value + (var - start)
    if temp == -1:
        temp = var
    return temp

def MapValidation(begin, range, dictionary):
    end = begin + range
    for start in dictionary:
        tempArr = list(dictionary.get(start))
        length = tempArr[1]
        if start <= begin and (start + length) <= end:
            return [begin, (start + length)]
        elif begin <= start and end <= (start + length):
            return [start, end]
        else:
            return False

def RangeTranslation(inputArray, transArray):
    newArray = []
    for range in inputArray:
        startValueIn = range[0]
        endValueIn = range[1]
        for stretch in transArray:
            tRange = stretch[0]
            startValueT = int(tRange[0])
            endValueT = int(tRange[1])
            transform = int(stretch[1])
            print(f'Seed range = {startValueIn} - {endValueIn}')
            print(f'Transform range = {startValueT} - {endValueT}')
            #input forward overlap with Trans
            b4Chunk = []
            chunk = []
            afterChunk = []
            if startValueIn <= startValueT and startValueT <= endValueIn:
                chunk = [(startValueT + transform), (endValueIn + transform)]
                if startValueIn < startValueT:
                    b4Chunk = [startValueIn, (startValueT - 1)]
                if b4Chunk != "None":
                    newArray.append(b4Chunk)
                newArray.append(chunk)
            #input back overlap with trans
            elif (startValueT <= startValueIn <= endValueT):
                chunk = [(startValueIn + transform), (endValueT + transform)]
                if
                afterChunk = [(endValueT - 1), endValueIn]
                newArray.append(chunk)
                if afterChunk != "None":
            #input no trans overlap

            elif (int(endValueT) < startValueIn) or (endValueIn < int(startValueT)):

                pass

minLoc = 'None'
'''
for seed in seedsList:
    soil = MapTranslation(int(seed), seedsToSoilMap)
    fertilizer = MapTranslation(soil, soilToFertilizer)
    water = MapTranslation(fertilizer, fertilizerToWater)
    light = MapTranslation(water, waterToLight)
    temp = MapTranslation(light, lightToTemperature)
    humidity = MapTranslation(temp, tempToHumidity)
    location = MapTranslation(humidity, humidityToLoc)
    #print(f'seed = {seed}, soil = {soil}, fertilizer = {fertilizer}, water = {water}, light = {light}, temp = {temp}, humidity = {humidity}, Location = {location}')
    if minLoc == 'None':
        minLoc = location
    if location < minLoc:
        minLoc = location
'''
part2Loc = 0
print(seedRange)
print(seedsToSoilRange)
RangeTranslation(seedRange, seedsToSoilRange)
'''
print(soilToFertRange)
print(fertToWaterRange)
print(waterToLightRange)
print(lightToTempRange)
print(tempToHumidityRange)
print(humidityToLocRange)
'''

#correct awnser for test data 1 is 35
print(f'Lowest location number = {minLoc}')
print(f'Part 2 location number = {part2Loc}')