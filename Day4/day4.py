neighbors = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
res = 0

def check(y, x, grid, word, direction):
    is_match = True
    for i in range(len(word)):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != word[i]:
            is_match = False
            break

        y += direction[0]
        x += direction[1]

    return is_match         

def part1():
    global res

    grid = []
    with open("day4.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for direction in neighbors:
                if check(i, j, grid, direction):
                    res += 1

def part2():
    global res

    grid = []
    with open("day4.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    words = [("SAM", "MAS"), ("MAS", "SAM"), ("SAM", "SAM"), ("MAS", "MAS")]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for word in words:
                if check(i, j, grid, word[0], [1, 1]) and check(i, j + 2, grid, word[1], [1 , -1]):
                    res += 1
                

part2()
print(res)