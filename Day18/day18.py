from collections import deque


def part1():
    grid = [["."] * 71 for _ in range(71)]
    # for row in open("day18.in").read().split("\n"):
    #     grid.append(list(row.strip()))

    bytes = [list(map(int, coords.split(","))) for coords in open("day18.in").read().split("\n")]
    for i in range(1024):
        x, y = bytes[i]
        grid[y][x] = "#"
    
    q = deque()

    q.append((0, 0))
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    res = 0
    found_end = False
    while q:
        size = len(q)

        for i in range(size):
            y, x = q.popleft()
            visited.add((y, x))
            
            if (y, x) == (70, 70):
                found_end = True
                break

            for n in neighbors:
                n_y, n_x = y + n[0], x + n[1]

                if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or (n_y, n_x) in visited or grid[n_y][n_x] == "#":
                    continue
                
                visited.add((n_y, n_x))
                q.append((n_y, n_x))

        if found_end:
            break
            
        res += 1 
        
    print(res)    
        
    for row in grid:
        print(''.join(row))

def bfs(grid):
    q = deque()
    q.append((0, 0))
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    res = 0
    found_end = False
    while q:
        size = len(q)

        for i in range(size):
            y, x = q.popleft()
            visited.add((y, x))
            
            if (y, x) == (70, 70):
                found_end = True
                break

            for n in neighbors:
                n_y, n_x = y + n[0], x + n[1]

                if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid[0]) or (n_y, n_x) in visited or grid[n_y][n_x] == "#":
                    continue
                
                visited.add((n_y, n_x))
                q.append((n_y, n_x))

        if found_end:
            break
            
        res += 1 
    
    return found_end

def part2():
    grid = [["."] * 71 for _ in range(71)]
    # for row in open("day18.in").read().split("\n"):
    #     grid.append(list(row.strip()))

    bytes = [list(map(int, coords.split(","))) for coords in open("day18.in").read().split("\n")]
    res = (0, 0)
    for i in range(len(bytes)):
        x, y = bytes[i]
        grid[y][x] = "#"

        if not bfs(grid):
            res = (x, y)
            break

    print(res)

    
    q = deque()          
        
    # for row in grid:
    #     print(''.join(row))

part2()