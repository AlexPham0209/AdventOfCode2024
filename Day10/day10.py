
from collections import deque


def part2():
    grid = []
    with open("day10.in") as file:
        for line in file:
            grid.append(list(map(int, [i if i != "." else "-1" for i in list(line.strip())])))

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    res = 0
    visited_end = set()

    def backtrack(y, x):
        if grid[y][x] == 9:
            return 1
        
        visited[y][x] = True
        total = 0

        for n in neighbors:
            n_y, n_x = y + n[0], x + n[1]

            if n_y < 0 or n_y >= len(grid) or n_x < 0 or n_x >= len(grid):
                continue
        
            if grid[y][x] + 1 != grid[n_y][n_x] or not visited[y][x] or grid[y][x] == -1:
                continue

            total += backtrack(n_y, n_x)

        visited[y][x] = False
        return total
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                visited_end = set()
                res += backtrack(i, j)
                
    print(res)



part2()