with open("input.txt") as f:
    patterns = f.read().split("\n\n")

result = 0


def is_smudge_mirror(above, below):
    smudges = 0
    for r in range(len(above)):
        for c in range(len(above[0])):
            if above[r][c] != below[r][c]:
                smudges += 1
                if smudges > 1:
                    return False
    if smudges == 1:
        return True
    else:
        return False


def find_mirror(matrix):
    for row in range(1, len(matrix)):
        above = matrix[:row][::-1]
        below = matrix[row:]
        above = above[: len(below)]
        below = below[: len(above)]

        if is_smudge_mirror(above, below):
            return row
    return 0


for pattern in patterns:
    rows = pattern.split("\n")

    m = len(rows)
    n = len(rows[0])
    stack = []

    # Create a transposed copy of rows, ie rows of columns
    cols = [[] for _ in range(n)]
    for r in range(m):
        for c in range(n):
            char = rows[r][c]
            cols[c] += char

    result += find_mirror(rows) * 100 + find_mirror(cols)
    # if result == 0:
    #   print(pattern)

print(result)
