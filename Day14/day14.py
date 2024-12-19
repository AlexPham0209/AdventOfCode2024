from collections import defaultdict
from PIL import Image
import numpy as np

WIDTH = 101
HEIGHT = 103

class Robot:
    def __init__(self, y, x, v):
        self.y = y
        self.x = x
        self.v = v

    def move(self):
        self.y = (self.y + self.v[0]) % HEIGHT
        self.x = (self.x + self.v[1]) % WIDTH
        return (self.y, self.x)
        
def part1():
    robots = []
    with open("day14.in") as file:
        for line in file:
            p, v = line[2:].split()
            x, y = map(int, p.split(","))
            vx, vy = map(int, v[2:].split(","))

            robots.append(Robot(y, x, (vy, vx)))

    positions = {}
    for i in range(100):
        temp = defaultdict(int)
        for robot in robots:
            temp[robot.move()] += 1
    
        positions = temp

    quadrants = [
        [(0, 0), (HEIGHT//2, WIDTH//2)], 
        [(0, WIDTH//2 + 1), (HEIGHT//2,WIDTH)], 
        [(HEIGHT//2 + 1, 0), (HEIGHT, WIDTH//2)], 
        [(HEIGHT//2 + 1, WIDTH//2 + 1), (HEIGHT, WIDTH)]
    ]

    res = 1
    for quadrant in quadrants:
        start, end = quadrant
        amount = 0
        for i in range(start[0], end[0]):
            for j in range(start[1], end[1]):
                if (i, j) in positions:
                    amount += positions[(i, j)]

        res *= amount

    print(res)

def get_width(y, x, positions):
    l = x
    while (y, l) in positions:
        l -= 1

    r = x
    while (y, r) in positions:
        r += 1

    return (l + 1, r - 1)

def part2():
    robots = []
    positions = defaultdict(int)
    with open("day14.in") as file:
        for line in file:
            p, v = line[2:].split()
            x, y = map(int, p.split(","))
            vx, vy = map(int, v[2:].split(","))

            robots.append(Robot(y, x, (vy, vx)))
            positions[(y, x)] += 1

   
    for i in range(30001):
        grid = [[255] * WIDTH for _ in range(HEIGHT)]
        for robot in robots:
            grid[robot.y][robot.x] = 0
        
        arr = np.array(grid, dtype=np.uint8)
        img = Image.fromarray(arr)
        img.save(f"C:/Users/RedAP/Desktop/Programming Projects/AdventOfCode/Day14/images/{i + 1}.png")

        temp = defaultdict(int)
        for robot in robots:
            temp[robot.move()] += 1

        positions = temp
  
part2()
