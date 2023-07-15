with open('input.txt', 'r') as file:
    result: int = 0
    total: int = 0
    for line in file:
        try:
            total += int(line)
        except ValueError:
            if total > result:
                result = total

            total = 0
            continue

print(result)
