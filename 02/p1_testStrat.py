# a = 2  # a > 3, b > 6, c > 0
# b = 3  # a > 0, b > 3, c > 6
# c = 4  # a > 6, b > 0, c > 3
# print((a - a) % 3, 'D')  # D
# print((a - b) % 3, 'W')  # W
# print((a - c) % 3, 'L')  # L
#
# print((b - a) % 3, 'L')  # L
# print((b - b) % 3, 'D')  # D
# print((b - c) % 3, 'W')  # W
#
# print((c - a) % 3, 'W')  # W
# print((c - b) % 3, 'L')  # L
# print((c - c) % 3, 'D')  # D


# print(0, ' is a W')
# print(1, ' is a D')
# print(2, ' is a L')

with open('input.txt', 'r') as file:
    result = 0
    for line in file:
        choice = (ord(line[2]) - 1) % 3 + 1
        round = ((ord(line[2]) - (ord(line[0]))) - 1) % 3 * 3
        result += choice + round
# print()
# print()
# print()
# # print((ord(line[0]) - 1))
# print(((ord('X') - (ord('A') - 1)) - 2) % 3)
# print(((ord('Y') - (ord('A') - 1)) - 2) % 3)
# print(((ord('Z') - (ord('A') - 1)) - 2) % 3)
# print()
# print()
