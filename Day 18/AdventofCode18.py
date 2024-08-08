pointsArray = [(0,0)]

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}
#b = boundry points
b = 0

for line in open('input18'):
    d, n, _ = line.split()
    dr, dc = directions[d]
    n = int(n)
    b += n
    r, c = pointsArray[-1]
    pointsArray.append((r + dr * n, c + dc * n))

#print(pointsArray)

#Shoelace forumla recommended by hints  a = area
a = abs(sum(pointsArray[i][0] * (pointsArray[i - 1][1] - pointsArray[(i + 1) % len(pointsArray)][1]) for i in range(len(pointsArray))))  // 2

#Pick's Theorem was also recommended
i = a - b // 2 + 1

print(f"The area of our trench is {i + b}.")


