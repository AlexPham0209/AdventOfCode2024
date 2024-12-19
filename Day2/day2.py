reports = []

with open('day2.in') as file:
    for line in file:
        reports.append(list(map(int, line.split())))


res = 0

for level in reports:
    is_safe = True

    if level[0] < level[1] and (abs(level[0] - level[1]) >= 1 and abs(level[0] - level[1]) <= 3):
        for i in range(1, len(level) - 1):
            if level[i] >= level[i + 1] or (abs(level[i] - level[i + 1]) < 1 or abs(level[i] - level[i + 1]) > 3):
                is_safe = False
                break

    elif level[0] > level[1] and (abs(level[0] - level[1]) >= 1 and abs(level[0] - level[1]) <= 3):
        for i in range(1, len(level) - 1):
            if level[i] <= level[i + 1] or (abs(level[i] - level[i + 1]) < 1 or abs(level[i] - level[i + 1]) > 3):
                is_safe = False
                break

    else:
        is_safe = False
    
    if is_safe:
        res += 1

print(res) 