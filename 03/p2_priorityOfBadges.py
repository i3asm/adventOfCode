def get_letter_priority(letter: str):
    if letter > 'Z':
        return ord(letter) - 96
    else:
        return ord(letter) - 38  # sum of -64 for letter index and +26 from the question, A-Z is 27-52


with open('input.txt', 'r') as file:
    res = 0
    groupIndex = 0
    groupSack = {}  # map of the letters found
    for line in file:
        elfSack = {}
        line: str = line.split('\n')[0]  # removing \n character
        for letter in line:
            elfSack[letter] = True

        # register items in the elf's sack as items for the group's sack
        for item in elfSack:
            if groupSack.get(item):
                groupSack[item] += 1
            else:
                groupSack[item] = 1

        # we got to the third elf
        if groupIndex == 2:
            for item in groupSack:
                if groupSack.get(item) == 3:
                    res += get_letter_priority(item)
                    break
            groupSack = {}
            groupIndex = 0
        else:
            groupIndex += 1

    print(res)
