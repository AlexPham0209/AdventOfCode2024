from collections import Counter, defaultdict
import copy
import math


# def part1():
#     stones = list(map(int, open("day11.in").read().split()))
    
#     for i in range(25):
#         temp = []
        
#         for stone in stones:
#             if stone == 0:
#                 temp.append(1)
            
#             elif len(str(stone)) % 2 == 0:
#                 temp.append(int(str(stone)[:len(str(stone))//2]))
#                 temp.append(int(str(stone)[len(str(stone))//2:]))
            
#             else:
#                 temp.append(stone * 2024)
            
#             stones = temp
    
#     print(len(stones))

                
# def part2():
#     stones = list(map(int, open("day11.in").read().split()))
#     counts = defaultdict(int)
#     res = 0

#     for i in range(len(stones)):
#         counts[stones[i]] += 1 

#     for i in range(75):
#         temp = defaultdict(int)
#         for num in counts:
#             temp[num] = counts[num]

#         for num in counts:
#             if num == 0:
#                 temp[1] += counts[num]

#             elif len(str(num)) % 2 == 0:
#                 temp[int(str(num)[:len(str(num))//2])] += counts[num]
#                 temp[int(str(num)[len(str(num))//2:])] += counts[num]
                
#             else:
#                 temp[num * 2024] += counts[num]
            
#             temp[num] -= counts[num]
#             if temp[num] <= 0:
#                 del temp[num]
        
#         counts = temp

#     res = 0
#     for num in counts:
#         res += counts[num]

#     print(res)

dp = dict()

def count(n, d):
    if d == 0:
        return 1 
    
    if (n, d) in dp:
        return dp[(n, d)] 

    if n == 0:
        dp[(n, d)] = count(1, d - 1)
        return dp[(n, d)]
    
    di = math.floor(math.log(n, 10)) + 1
    if di % 2 == 0:
        dp[(n, d)] = count(n // (10 ** (di//2)), d - 1) + count(n % (10 ** (di//2)), d - 1)
        return dp[(n, d)]
    
    dp[(n, d)] = count(2024 * n, d - 1)
    return dp[(n, d)]
        
stones = list(map(int, open("day11.in").read().split()))
res = 0    

for stone in stones:
    res += count(stone, 250)

print(res)