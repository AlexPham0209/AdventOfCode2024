d = {
    "^" : 0,
    "v" : 1,
    "<" : 2,
    ">" : 3 
}

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def part1():
    rows, inputs = open("day15.in").read().split("\n\n")
    grid = [list(r) for r in rows.split("\n")]
    input = ''.join(inputs.split("\n"))

    y, x = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                y, x = i, j
    
    f = open("day15.out", "w")
    for i in range(len(input)):
        curr = directions[d[input[i]]]
        n_y, n_x = y + curr[0], x + curr[1]

        if grid[n_y][n_x] == "#":
            continue
        
        t_y = n_y
        t_x = n_x
        while grid[t_y][t_x] == "O":
            t_y += curr[0]
            t_x += curr[1]
        
        if grid[t_y][t_x] == "#":
            continue
        
        while (t_y, t_x) != (y, x):
            temp = grid[t_y - curr[0]][t_x - curr[1]]
            grid[t_y - curr[0]][t_x - curr[1]] = grid[t_y][t_x]
            grid[t_y][t_x] = temp
            
            t_y -= curr[0]
            t_x -= curr[1]
        
        grid[n_y][n_x] = "@"
        grid[y][x] = "."
        y, x = n_y, n_x

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                res += i * 100 + j
    
    print(res)

def scale_grid(s_grid):
    grid = []
    for i in range(len(s_grid)):
        row = []
        for j in range(len(s_grid[i])):
            if s_grid[i][j] == "#":
                row.append("#")
                row.append("#")
            
            elif s_grid[i][j] == "O":
                row.append("[")
                row.append("]")
            
            elif s_grid[i][j] == ".":
                row.append(".")
                row.append(".")

            else:
                row.append("@")
                row.append(".")
        
        grid.append(row)

    return grid

def dfs(y, x, dir, grid, boxes):
    if (y, x) in boxes:
        return
    
    neighbors = set()
    neighbors.add((y, x))
    boxes.add((y, x))

    match dir:
        case (0, -1):
            if grid[y][x - 1] == "[" or grid[y][x - 1] == "]":
                neighbors.add((y, x - 1))
                boxes.add((y, x - 1))
        
        case (0, 1):
            if grid[y][x + 1] == "[" or grid[y][x + 1] == "]":
                neighbors.add((y, x + 1))
                boxes.add((y, x + 1))

        case _:
            if grid[y][x] == "[":
                neighbors.add((y, x + 1))
                boxes.add((y, x + 1))
            else:
                neighbors.add((y, x - 1))
                boxes.add((y, x - 1))
    
    
    for n in neighbors: 
        n_y, n_x = n[0] + dir[0], n[1] + dir[1]

        if (grid[n_y][n_x] == "[" or grid[n_y][n_x] == "]") and (n_y, n_x) not in boxes:
            dfs(n_y, n_x, dir, grid, boxes)
        
def check_collision(points, dir, grid):
    for point in points:
        y, x = point
        n_y, n_x = y + dir[0], x + dir[1]

        if (n_y, n_x) not in points and grid[n_y][n_x] != ".":
            return True
        
    return False

def move(points, dir, grid):
    moved = set()
    for point in points:
        y, x = point
        moved.add((grid[y][x], (y + dir[0], x + dir[1])))
        grid[y][x] = "."

    for point in moved:
        c, coord = point
        y, x = coord
        grid[y][x] = c

def part2():
    rows, inputs = open("day15.in").read().split("\n\n")
    grid = scale_grid([list(r) for r in rows.split("\n")])
    input = ''.join(inputs.split("\n"))

    y, x = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                y, x = i, j

    for i in range(len(input)):
        curr = directions[d[input[i]]]
        n_y, n_x = y + curr[0], x + curr[1]

        if grid[n_y][n_x] == "#":
            continue

        boxes = set()
        if grid[n_y][n_x] == "[" or grid[n_y][n_x] == "]":
            dfs(n_y, n_x, curr, grid, boxes)
        
        if check_collision(boxes, curr, grid):
            continue
        
        move(boxes, curr, grid)
        grid[y][x] = "."
        grid[n_y][n_x] = "@"
        y, x = n_y, n_x

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                res += i * 100 + j

    for row in grid:
        print(''.join(row))
    print()
    print(res)

part2()

