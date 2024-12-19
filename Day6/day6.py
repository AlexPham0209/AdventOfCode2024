from collections import defaultdict
import time


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

facing = {
    "^" : 0,
    ">" : 1,
    "v" : 2,
    "<" : 3,
}


def part1():
    grid = []
    curr = 0
    y = 0
    x = 0

    with open("day6.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "." and grid[i][j] != "#":
                y = i
                x = j
                curr = facing[grid[i][j]]

    while y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]):
        grid[y][x] = "X"
        dir = directions[curr]
        
        n_y = y + dir[0]
        n_x = x + dir[1]

        if n_y < 0 or n_y >= len(grid) or n_x < 0 and n_x >= len(grid[0]):
            break

        if grid[n_y][n_x] == "#":
            curr = (curr + 1) % len(directions)
        else:
            y = n_y 
            x = n_x
    
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                res += 1

    print(res)


def check(start, curr, grid):
    y, x = start
    visited = defaultdict(set)

    while y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]):
        if (y, x) in visited and directions[curr] in visited[(y, x)]:
            return True

        visited[(y, x)].add(directions[curr])
        dir = directions[curr]
        
        n_y = y + dir[0]
        n_x = x + dir[1]

        if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]):
            break

        if grid[n_y][n_x] == "#":
            curr = (curr + 1) % len(directions)
        else:
            y = n_y 
            x = n_x

    return False

def part2():
    grid = []
    curr = 0
    y = 0
    x = 0
    res = 0

    start = time.time()
    with open("day6.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "." and grid[i][j] != "#":
                y = i
                x = j
                curr = facing[grid[i][j]]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                
                if check((y, x), curr, grid):
                    res += 1
                
                grid[i][j] = "."

    print(res)
    print(time.time() - start)

part2()