with open('input.txt') as f:
  rows = f.read().split('\n')

total = 0
symbols = {'$', '&', '-', '+', '=', '#', '@', '/', '%', '*'}
curr_num = ''
is_part = False
directions = [
  [-1, -1],
  [0, -1],
  [1, -1],
  [-1, 0],
  [1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
]

def check_for_symbols(m, n):
  for d in directions:
    new_r = m + d[0]
    new_c = n + d[1]
    if new_r in range(len(rows)) and new_c in range(len(rows[m])):
      if rows[new_r][new_c] in symbols:
        return True
  return False

for m in range(len(rows)):
  row = rows[m]
  for n in range(len(row)):
    c = row[n]
    if c.isdigit():
      # check for adjacent symbol.
      if not is_part:
        is_part = check_for_symbols(m, n)
      curr_num += c
    else:
      if curr_num and is_part:
        total += int(curr_num)
      curr_num = ''
      is_part = False

print(total)
