import math


def backtrack(i, curr, terms, res):
    if i >= len(terms):
        return curr == res

    total = 0
    total += backtrack(i + 1, curr * terms[i], terms, res)
    total += backtrack(i + 1, curr + terms[i], terms, res)

    return total

def backtrack2(i, total, terms):
    if total < 0:
        return 0

    if i >= len(terms):
        return total == 0

    res = 0
    if total % terms[i] == 0:
        res += backtrack2(i + 1, total // terms[i], terms)
    
    res += backtrack2(i + 1, total - terms[i] if i != 0 else terms[i], terms)

    concat = total * (10 ** (math.floor(math.log(terms[i], 10) + 1))) + terms[i]
    res += backtrack2(i + 1, concat, terms)

    return res



def part1():
    res = 0
    with open("day7.in") as file:
        for line in file:
            case = line.strip().split(": ")
            total = int(case[0])
            terms = list(map(int, case[1].split()))

            ways = backtrack(0, 1, terms, total)

            if ways > 0:
                res += total 

    print(res)

def part2():
    res = 0
    with open("day7.in") as file:
        for line in file:
            case = line.strip().split(": ")
            total = int(case[0])
            terms = list(map(int, case[1].split()))

            ways = backtrack2(0, 1, terms, total, dict())
            if ways > 0:
                res += total 

    print(res)


part2()