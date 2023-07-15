def get_letter_priority(char: str):
    if char > 'Z':
        return ord(char) - 96
    else:
        return ord(char) - 38  # sum of -64 for letter index and +26 from the question, A-Z is 27-52


with open('input.txt', 'r') as file:
    wrongItemsTotal = 0
    for line in file:
        line: str = line.split('\n')[0]  # removing \n character
        middle: int = int(len(line) / 2)
        firstHalf = line[:middle]
        secondHalf = line[middle:]
        firstSack = {}  # map of the letters found
        for char in firstHalf:
            firstSack[char] = True
        for char in secondHalf:
            if firstSack.get(char):
                wrongItemsTotal += get_letter_priority(char)
                break

    print(wrongItemsTotal)
