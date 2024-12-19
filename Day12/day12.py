from collections import defaultdict, deque
neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]

f = open("day12.out", "w")   

def bfs(y, x, grid, visited):
    q = deque()
    q.append((y, x))
    points = set()
    type = grid[y][x]
    visited.add((y, x))

    while q:
        y, x = q.popleft()
        points.add((y, x))

        for n in neighbors:
            n_y, n_x = y + n[0], x + n[1]

            if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]):
                continue

            if (n_y, n_x) in visited or grid[n_y][n_x] != type:
                continue
            
            visited.add((n_y, n_x))
            q.append((n_y, n_x))

    return points

        
def part1():
    grid = [list(row.strip()) for row in open("day12.in")]
    regions = defaultdict(set)
    visited = set()
    islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in visited:
                points = bfs(i, j, grid, visited)
                regions[(islands, grid[i][j])] = points

                islands += 1

    res = 0
    for plant in regions:
        type = plant[1]
        points = regions[plant]
        area = len(points)
        perimeter = 0

        for point in points:
            y, x = point

            for n in neighbors:
                n_y, n_x = y + n[0], x + n[1]

                if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or grid[n_y][n_x] != type:
                    perimeter += 1

        res += perimeter * area

    print(res)

count = 0

direction = {
    0 : "UP",
    1 : "LEFT",
    2 : "DOWN",
    3 : "RIGHT"
}

def dfs(y, x, dir, perimeter, visited):
    visited.add((y, x, dir))

    neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for n in neighbors:
        n_y, n_x = y + n[0], x + n[1]
        
        if (n_y, n_x, dir) not in visited and (n_y, n_x, dir) in perimeter:
            visited.add((n_y, n_x, dir))
            dfs(n_y, n_x, dir, perimeter, visited)

def part2():
    grid = [list(row.strip()) for row in open("day12.in")]
    regions = defaultdict(set)
    visited = set()
    islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in visited:
                points = bfs(i, j, grid, visited)
                regions[(islands, grid[i][j])] = points

                islands += 1

    res = 0

    for plant in regions:
        type = plant[1]
        points = regions[plant]
        area = len(points)
        perimeter = set()

        for point in points:
            edges = 0
            y, x = point    

            neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for i, n in enumerate(neighbors):
                n_y, n_x = y + n[0], x + n[1]

                if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or (n_y, n_x) not in points:
                    perimeter.add((n_y, n_x, i))

        visited = set()
        sides = 0

        for node in perimeter:
            if node not in visited:
                sides += 1 
                y, x, dir = node
                dfs(y, x, dir, perimeter, visited)
                
        res += sides * area

    print(res)

part2()
