import re

def part1():
    res = 0
    arr = []

    with open('day3.in') as file:
        for line in file:
            values = re.findall("mul\(\d+,\d+\)", line)
            for value in values:
                a, b = map(int, value[4:(len(value) - 1)].split(","))
                arr.append([a,b])
                res += a * b

    print(res)
    return arr
    
def part1_alt():
    res = 0
    arr = []

    with open('day3.in') as file:
        for line in file:
            indices = [i.end() for i in re.finditer("mul\(", line)]

            for index in indices:
                values = []
                num = ""

                while index < len(line) and line[index] != ")":
                    if not line[index].isnumeric() and line[index] != ",":
                        break

                    if line[index] == "," and len(values) < 1:
                        values.append(int(num))
                        num = ""
                    
                    else:
                        num += line[index]
                    
                    index += 1
                    
                if index < len(line) and line[index] == ")":
                    values.append(int(num))

                if len(values) == 2:
                    arr.append([values[0],values[1]])
                    res += values[0] * values[1]
    
    print(res)
    return arr

def part2():
    res = 0

    with open('day3.in') as file:
        stop = False
        for line in file:
            values = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
            for value in values:
                if value == "do()":
                    stop = False
                
                elif value == "don't()":
                    stop = True

                elif not stop:  
                    a, b = map(int, value[4:(len(value) - 1)].split(","))
                    res += a * b
                
        print(res)


a = part1()
b = part1_alt()

res = []
for i in range(len(b)):
    if b[i] not in a:
        res.append(b[i])

print(res)