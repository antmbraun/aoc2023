with open('input.txt') as f:
  rows = f.read().split('\n')

total = 0
curr_num = ''
gear = False
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

gears = {}

def check_for_star(m, n):
  for d in directions:
    new_r = m + d[0]
    new_c = n + d[1]
    if new_r in range(len(rows)) and new_c in range(len(rows[m])):
      if rows[new_r][new_c] == '*':
        index = str(new_r) + str(new_c)
        return index
  return False

for m in range(len(rows)):
  row = rows[m]
  for n in range(len(row)):
    c = row[n]
    if c.isdigit():
      # check for adjacent symbol.
      if not gear:
        gear = check_for_star(m, n)
      curr_num += c
    else:
      if curr_num and gear:
        curr_num = int(curr_num)
        if gear not in gears:
          gears[gear] = {
            'count': 1,
            'ratio': curr_num
          }
        else:
          gears[gear]['count'] += 1
          gears[gear]['ratio'] *= curr_num
         
      curr_num = ''
      gear = False

for gear in gears.values():
  print(gear)
  if gear['count'] == 2:
    total += gear['ratio']
    
print(total)
