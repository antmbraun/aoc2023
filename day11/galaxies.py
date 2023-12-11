with open('input.txt') as f:
  rows = f.read().split('\n')


m = len(rows)
n = len(rows[0])
total = 0


# Find empty rows and columns.
empty_rows = [1] * m
empty_cols = [1] * n

for r in range(m):
  for c in range(n):
    if rows[r][c] == '#':
      empty_rows[r] = 0
      empty_cols[c] = 0

# Expand the universe via copy.
expanded_universe = []
for r in range(m):
  expanded_universe.append([])
  for c in range(n):
    char = rows[r][c] 
    expanded_universe[-1].append(char)
    if empty_cols[c] == 1:
      expanded_universe[-1].append(char)
  if empty_rows[r] == 1:
    expanded_universe.append(expanded_universe[-1].copy())

# Get the coordinates of all the galaxies.
galaxies = []

for m in range(len(expanded_universe)):
  for n in range(len(expanded_universe[0])):
    c = expanded_universe[m][n]
    if c == '#':
      galaxies.append([m, n])

for g1 in galaxies:
  for g2 in galaxies:
    d = abs((g2[0] - g1[0])) + abs((g2[1] - g1[1]))
    total += d

print(total // 2)



  

    