# a = 2  # a > 3, b > 6, c > 0
# b = 3  # a > 0, b > 3, c > 6
# c = 4  # a > 6, b > 0, c > 3
# print((a - x) % 3, 'D')  # D
# print((a - y) % 3, 'W')  # W
# print((a - z) % 3, 'L')  # L

# print((b - x) % 3, 'L')  # L
# print((b - y) % 3, 'D')  # D
# print((b - z) % 3, 'W')  # W

# print((c - x) % 3, 'W')  # W
# print((c - y) % 3, 'L')  # L
# print((c - z) % 3, 'D')  # D

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
