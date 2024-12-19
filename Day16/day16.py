from collections import defaultdict, deque
import heapq


def part1():
    grid = []
    with open("day16.in") as file:
        for line in file:
            grid.append(list(line.strip()))
    
    q = []
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    
    distances = dict()
    prev = dict()
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                distances[(i, j, 3)] = (0, 0, 0)
                heapq.heappush(q, [0, i, j, 3])

    end = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "E":
                end = (i, j)

    curr = (0, 0, 0)
    f = open("day16.out", "w")
    while q:
        dist, y, x, dir = heapq.heappop(q)

        if (y, x, dir) in visited:
            continue

        if (y, x) == end:
            curr = (y, x, dir) 
            res = dist
            break
            

        visited.add((y, x, dir))

        for i, n in enumerate(neighbors):
            n_y, n_x = y + n[0], x + n[1]
            total, dist, turns = distances[(y, x, dir)]

            d = dist + 1
            t = turns + 1 if i != dir else turns
            temp = t * 1000 + d

            if (n_y, n_x, i) in visited:
                continue

            if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or grid[n_y][n_x] == "#":
                continue
            
            if (n_y, n_x, i) not in distances or temp <= distances[(n_y, n_x, i)][0]:
                distances[(n_y, n_x, i)] = (temp, d, t)
                prev[(n_y, n_x, i)] = (y, x, dir)

                heapq.heappush(q, [temp, n_y, n_x, i])


    print(res)

def dfs(curr, prev, grid, amount):
    if curr not in prev:
        return
    
    grid[curr[0]][curr[1]] = "O"
    amount.add(curr)

    for n in prev[curr]:
        dfs(n, prev, grid, amount) 

def part2():
    grid = []
    with open("day16.in") as file:
        for line in file:
            grid.append(list(line.strip()))
    
    q = []
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    
    distances = dict()
    prev = defaultdict(set)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                distances[(i, j, 3)] = (0, 0, 0)
                heapq.heappush(q, [0, i, j, 3])

    end = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "E":
                end = (i, j)

    curr = (0, 0, 0)
    f = open("day16.out", "w")
    paths = set()
    while q:
        dist, y, x, dir = heapq.heappop(q)

        if (y, x, dir) in visited:
            continue

        if (y, x) == end:
            curr = (y, x, dir) 
            res = dist
            break
            
        visited.add((y, x, dir))

        for i, n in enumerate(neighbors):
            n_y, n_x = y + n[0], x + n[1]
            total, dist, turns = distances[(y, x, dir)]
            
            d = dist + 1
            t = turns + 1 if i != dir else turns
            temp = t * 1000 + d

            if (n_y, n_x, i) in visited:
                continue

            if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or grid[n_y][n_x] == "#":
                continue
            
            if (n_y, n_x, i) not in distances or temp <= distances[(n_y, n_x, i)][0]:
                if (n_y, n_x, i) in distances and temp < distances[(n_y, n_x, i)][0]:
                    prev[(n_y, n_x, i)] = set()
                    
                prev[(n_y, n_x, i)].add((y, x, dir))
            
                distances[(n_y, n_x, i)] = (temp, d, t)

                heapq.heappush(q, [temp, n_y, n_x, i])

    amount = set()
    dfs(curr, prev, grid, amount)
    
    res = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                res += 1 

    print(res)
            


part2()