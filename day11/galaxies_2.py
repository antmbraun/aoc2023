with open('input.txt') as f:
  rows = f.read().split('\n')


m = len(rows)
n = len(rows[0])
total = 0
galaxies = []

# Find empty rows and columns and find the galaxies.
empty_rows = [1] * m
empty_cols = [1] * n

for r in range(m):
  for c in range(n):
    if rows[r][c] == '#':
      empty_rows[r] = 0
      empty_cols[c] = 0
      galaxies.append([r, c])

def get_distance(g1, g2):
    distance = 0
    # Traverse from g1 row to g2 row counting steps.
    g1row, g2row = g1[0], g2[0]
    row_range = range(min(g1row, g2row), max(g1row, g2row) + 1)
    distance += sum(1000000 if empty_rows[step] else 1 for step in row_range) - 1 if g1row != g2row else 0

    # Traverse from g1 col to g2 col counting steps
    g1col, g2col = g1[1], g2[1]
    col_range = range(min(g1col, g2col), max(g1col, g2col) + 1)
    distance += sum(1000000 if empty_cols[step] else 1 for step in col_range) - 1 if g1col != g2col else 0

    return distance

start = 1
for g1 in galaxies:
  for i in range(start, len(galaxies)):
    g2 = galaxies[i]
    d = get_distance(g1, g2)
    total += d
  start += 1

print(total)
    