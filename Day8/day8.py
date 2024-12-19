from collections import defaultdict

def in_bounds(point, grid):
    return point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0])

def part1():
    grid = []
    res = 0
    with open("day8.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    frequencies = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != ".":
                frequencies[grid[i][j]].append((i, j))
    
    for f in frequencies:
        points = frequencies[f]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b = [points[i], points[j]]
                dy = b[0] - a[0]
                dx = b[1] - a[1]

                c = (a[0] - dy, a[1] - dx)
                d = (b[0] + dy, b[1] + dx)
                
                if in_bounds(c, grid) and (grid[c[0]][c[1]] != "#"):
                    grid[c[0]][c[1]] = "#"
                    res += 1
                
                if in_bounds(d, grid) and (grid[d[0]][d[1]] != "#"):
                    grid[d[0]][d[1]] = "#"
                    res += 1

    for row in grid:
        print(''.join(row))
    print(res)

def part2():
    grid = []
    res = 0
    with open("day8.in") as file:
        for line in file:
            grid.append(list(line.strip()))

    frequencies = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != ".":
                frequencies[grid[i][j]].append((i, j))
    
    for f in frequencies:
        points = frequencies[f]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b = [points[i], points[j]]
                dy = b[0] - a[0]
                dx = b[1] - a[1]

                y, x = a

                while in_bounds((y, x), grid):
                    if grid[y][x] != "#":
                        grid[y][x] = "#"
                        res += 1
                    y -= dy
                    x -= dx

                y, x = b
                while in_bounds((y, x), grid):
                    if grid[y][x] != "#":
                        grid[y][x] = "#"
                        res += 1
                    y += dy
                    x += dx

    for row in grid:
        print(''.join(row))
    print(res)

part2()
                

