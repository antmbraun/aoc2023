with open('input.txt') as f:
    cards = f.read().split('\n')

result = 0

wins_by_card = {}

for card_idx, card in enumerate(cards):
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

    i = i + 2  # Move index to the first digit of your numbers.

    while i < len(card):
        c = card[i]
        if c.isdigit():
            curr_num += c
        if not c.isdigit() or i == len(card) - 1:
            if curr_num and int(curr_num) in winning_nums:
                win_count += 1
            curr_num = ''
        i += 1

    wins_by_card[card_idx] = win_count


def get_wins(card):
    wins = wins_by_card[card]
    additional_cards = 0
    for i in range(card + 1, card + wins + 1):
        additional_cards += get_wins(i)
    return 1 + additional_cards

for card in wins_by_card:
    result += get_wins(card)

print(result)
