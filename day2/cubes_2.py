total = 0

with open("input.txt") as f:
    games = f.read().split("\n")

def find_fewest_cubes(game_str):
    curr_num = ""

    # Initialize values to 1 so if a game never uses it color, it will have no effect on the product.
    blue = 1
    green = 1
    red = 1

    # Fast forward to space after ':' 
    i = game_str.find(":") + 1

    while i < len(game_str) - 1:
        c = game_str[i]

        if c == " ":
            i += 1
            continue
        
        # Store current number:
        while c.isdigit():
            curr_num += c
            i += 1
            c = game_str[i]

        if curr_num and type(curr_num) == str:
            curr_num = int(curr_num)

        # Case: blue:
        if c == "b":
            if curr_num > blue:
                blue = curr_num
            i += 4 # Fast-forward to end of "blue," 
            curr_num = ""

        # Check red:
        if c == "r":
            if curr_num > red:
                red = curr_num
            i += 3 # Fast-forward to end of "red,"
            curr_num = ""

        # Check green:
        if c == "g":
            if curr_num > green:
                green = curr_num
            i += 5 # Fast-forward to end of "green,"
            curr_num = ""

        i += 1

    return blue * red * green


for game_str in games:
    result = find_fewest_cubes(game_str)
    total += int(result)
