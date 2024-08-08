from heapq import heappush, heappop

heatMap = [list(map(int, line.strip())) for line in open("input17")]

seen = set()
"""
Manually add the starting point in our queue. Heat loss is first, because minimum value needs to be first to use 
heappush, and heappop, 0,0 for current location, 0,0 direction, steps taken = 0
"""
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    #hl = heatloss, r and c  = row and column, dr and dc = current direction we are travelling, n steps
    hl, r, c, dr, dc, n = heappop(pq)

    #break condition and since the queue has priority we do not need to evaluate the ending spot
    if r == len(heatMap) - 1 and c == len(heatMap[0]) - 1:
        print(hl)
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))

    if n < 3 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(heatMap) and 0 <= nc < len(heatMap[0]):
            heappush(pq, (hl + heatMap[nr][nc], nr, nc, dr, dc, n + 1))

    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < len(heatMap) and 0 <= nc < len(heatMap[0]):
                heappush(pq, (hl + heatMap[nr][nc], nr, nc, ndr, ndc, 1))
