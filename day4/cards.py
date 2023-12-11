with open('input.txt') as f:
  cards = f.read().split('\n')

result = 0

for card in cards:
  winning_nums = set()
  win_count = 0

  i = card.find(':') + 2
  c = card[i]
  curr_num = ''

  while c != '|':
    if c.isdigit():
      curr_num += c
    else:
      if curr_num:
        winning_nums.add(int(curr_num))
        curr_num = ''
    i += 1
    c = card[i]
  
  i = i + 2 # Move index to first digit of your numbers.

  while i < len(card): 
    c = card[i]
    if c.isdigit():
      curr_num += c
    if not c.isdigit() or i == len(card) - 1:
      if curr_num and int(curr_num) in winning_nums:
        win_count += 1
      curr_num = ''
    i += 1

  points = 2 ** (win_count - 1) if win_count > 0 else 0
  result += points

print(result)