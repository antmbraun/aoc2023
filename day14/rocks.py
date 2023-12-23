with open('input.txt') as f:
 input = f.read().split('\n')

# Transpose the grid
cols = list(map(list, zip(*input)))

col_len = len(cols[0])

result = 0
rounds = 0

colnum = 0
for col in cols:
  colnum +=1
  for idx in range(len(col) - 1, -1, -1):
    item = col[idx]
 
    if item == 'O':
      rounds += 1

    if item == '#' or idx == 0:
      if item == '#':
        idx += 1
      for row in range(idx, idx + rounds):
        weight = col_len - row
        result += weight

      rounds = 0
print(result)
   