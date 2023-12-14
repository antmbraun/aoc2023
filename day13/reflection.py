with open('input.txt') as f:
  patterns = f.read().split('\n\n')

result = 0

def find_lines_before_reflection(matrix):
  back = 1
  r = 1
  while r < len(matrix):
    if matrix[r] == matrix[r - back]:
      line_of_reflection = r
    while matrix[r] == matrix[r - back]:
      back += 2
      r += 1
      if r == len(matrix) or r - back <0:
        return line_of_reflection
    back = 1
    r += 1
  return 0

for pattern in patterns:
  rows = pattern.split('\n')

  m = len(rows)
  n = len(rows[0])
  stack = []

  # Create a transposed copy of rows, ie rows of columns
  cols = [ [] for _ in range(n) ]
  for r in range(m):
    for c in range(n):
      char = rows[r][c]
      cols[c] += char

  result += find_lines_before_reflection(rows) * 100 + find_lines_before_reflection(cols)

print(result)
