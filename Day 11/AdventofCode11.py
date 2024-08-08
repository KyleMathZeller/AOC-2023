galaxy_grid = open('input11').read().splitlines()

empty_rows = [r for r, row in enumerate(galaxy_grid) if all(ch == "." for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*galaxy_grid)) if all(ch == "." for ch in col)]

galaxies = [(r, c) for r, row in enumerate(galaxy_grid) for c, ch in enumerate(row) if ch == '#']

total = 0
expansion = 1000000

for i, (r1, c1) in enumerate(galaxies):
  for (r2, c2) in galaxies[:i]:
    for r in range(min(r1, r2), max(r1, r2)):
      total += expansion if r in empty_rows else 1
    for c in range(min(c1, c2), max(c1, c2)):
      total += expansion if c in empty_cols else 1

print(f'Sum of lengths = {total}')
