reports = []

with open('day2.in') as file:
    for line in file:
        reports.append(list(map(int, line.split())))


def distance(a, b):
    return abs(a - b) >= 1 and abs(a - b) <= 3

res = 0

for level in reports:
    is_safe_increasing = False
    is_safe_decreasing = False

    is_safe = True
    for i in range(len(level) - 1):
        if level[i] <= level[i + 1] or not distance(level[i], level[i + 1]):
            is_safe = False
            break
    
    if is_safe:
        is_safe_increasing = True
    
    is_safe = True
    for i in range(len(level) - 1):
        if level[i] >= level[i + 1] or not distance(level[i], level[i + 1]):
            is_safe = False
            break

    if is_safe:
        is_safe_decreasing = True

    for i in range(len(level)):
        temp = list(level)
        temp.pop(i)

        is_safe = True
        for i in range(len(temp) - 1):
            if temp[i] >= temp[i + 1] or not distance(temp[i], temp[i + 1]):
                is_safe = False
                break
        
        if is_safe:
            is_safe_increasing = True

    
    is_safe_decreasing = False
    for i in range(len(level)):
        temp = list(level)
        temp.pop(i)

        is_safe = True
        for i in range(len(temp) - 1):
            if temp[i] <= temp[i + 1] or not distance(temp[i], temp[i + 1]):
                is_safe = False
                break
        
        if is_safe:
            is_safe_decreasing = True


    if is_safe_increasing or is_safe_decreasing:
        print(level)
        res += 1 

print(res) 