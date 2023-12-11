constraints = {"red": 12, "green": 13, "blue": 14}
total = 0

with open("input.txt") as f:
    games = f.read().split("\n")

def check_game(game_str):
    curr_num = ""
    game_index = ""
    i = 5
    while i < len(game_str) - 1:
        c = game_str[i]

        if c == " ":
            i += 1
            continue

        # Get the game index:
        if not game_index:
            while c != ":":
                game_index += c
                i += 1
                c = game_str[i]

        # Store current number:
        while c.isdigit():
            curr_num += c
            i += 1
            c = game_str[i]

        if curr_num and type(curr_num) == str:
            curr_num = int(curr_num)

        # Check blue:
        if c == "b":
            if int(curr_num) > constraints["blue"]:
                return 0
            i += 4 # Fast-forward to end of "blue " 
            curr_num = ""

        # Check red:
        if c == "r":
            if int(curr_num) > constraints["red"]:
                return 0
            i += 3 # Fast-forward to end of "red "
            curr_num = ""

        # Check green:
        if c == "g":
            if int(curr_num) > constraints["green"]:
                return 0
            i += 5 # Fast-forward to end of "green "
            curr_num = ""

        i += 1

    return game_index


for game_str in games:
    result = check_game(game_str)
    total += int(result)

print(total)