# The Elf finishes helping with the tent and sneaks back over to you.
# "Anyway, the second column says how the round needs to end:
# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win. Good luck!"

def points(first: str, second: str) -> int:
    res = 0
    if second == 'X':
        res = ((ord(first) - 1) + 1) % 3 + 1
    if second == 'Y':
        res = ((ord(first) - 1) + 2) % 3 + 1
    if second == 'Z':
        res = ((ord(first) - 1) + 0) % 3 + 1
    return res


with open('input.txt', 'r') as file:
    result = 0
    for line in file:

        # result of this round
        round = (ord(line[2]) - 1) % 3 * 3
        # points from the choice I have to take
        choice = points(line[0], line[2])

        result += choice + round

    print(result)

# print()
# print(points('A', 'X'))  # 3
# print(points('A', 'Y'))  # 1
# print(points('A', 'Z'))  # 2
# print()
# print(points('B', 'X'))  # 1
# print(points('B', 'Y'))  # 2
# print(points('B', 'Z'))  # 3
# print()
# print(points('C', 'X'))  # 2
# print(points('C', 'Y'))  # 3
# print(points('C', 'Z'))  # 1
# # print()
# # print()
