#Test data
#timeList = [7, 15, 30]
#distanceList = [9, 40, 200]

#Test Data
time = 71530
goal = 940200

#Solution 1 data
#timeList = [54, 94, 65, 92]
#distanceList = [302, 1476, 1029, 1404]

#Solution 2 data
time = 54946592
goal = 302147610291404

'''
solution1 = 1
for time, goal in zip(timeList, distanceList):
    winCounter = 0
    for speed in range(1, time):
        distance = (time - speed) * speed
        if distance > goal:
            winCounter += 1
    solution1 *=winCounter

print(f'Solution 1 is {solution1}')
'''

winCounter = 0
for speed in range(1, time):
    distance = (time - speed) * speed
    if distance > goal:
        winCounter += 1
    elif winCounter:
        break

print(f'Solution 2 is {winCounter}')