
from collections import defaultdict


f = list()
s = defaultdict(int)

with open('day1.in') as file:
    for line in file:
        a, b = map(int, line.split("   "))
        f.append(a)
        s[b] += 1

f.sort()
res = 0 

for i in range(len(f)):
    res += f[i] * s[f[i]]

print(res)