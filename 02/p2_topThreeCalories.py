with open('input.txt', 'r') as file:
    result: [] = [0, 0, 0]
    total: int = 0
    for line in file:
        try:
            total += int(line)
        except ValueError:
            if total > result[0]:
                result[2] = result[1]
                result[1] = result[0]
                result[0] = total
            elif total > result[1]:
                result[2] = result[1]
                result[1] = total
            elif total > result[2]:
                result[2] = total

            total = 0
            continue

print(result[0])
print(result[0]+result[1]+result[2])
