from collections import deque
#deque is first in first out

mirror_grid = open('input16').read().splitlines()

def calculate(r, c, dr, dc):
    # row, column, delta-row, delta-column
    start = [(r, c, dr, dc)]
    seen = set()
    q = deque(start)

    while q:
        r, c, dr, dc = q.popleft()

        r += dr
        c += dc

        if r < 0 or r >= len(mirror_grid) or c < 0 or c >= len(mirror_grid[0]):
            continue

        char = mirror_grid[r][c]

        if char == "." or (char == "-" and dc != 0) or (char == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif char == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif char == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if char == '|' else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

    tiles = {(r, c) for (r, c, _, _) in seen}

    return len(tiles)

#Part one
print(f'Tiles energized for part one = {calculate(0, -1, 0, 1)}')

#Part two
max_val = 0

for row in range(len(mirror_grid)):
    max_val = max(max_val, calculate(row, -1, 0, 1))
    max_val = max(max_val, calculate(row, len(mirror_grid[0]), 0, -1))

for col in range(len(mirror_grid)):
    max_val = max(max_val, calculate(-1, col, 1, 0))
    max_val = max(max_val, calculate(len(mirror_grid), col, -1, 0))

print(f'Maximum energized tiles for part two = {max_val}')