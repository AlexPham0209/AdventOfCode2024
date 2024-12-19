import math

def part2():
    cases = open("day13.in").read().split("\n\n")
    res = 0

    for case in cases:
        a, b, prize = case.split("\n")
        a = a.split(": ")[1].split(", ")
        a = (int(a[0][2:]), int(a[1][2:]))

        b = b.split(": ")[1].split(", ")
        b = (int(b[0][2:]), int(b[1][2:]))

        prize = prize.split(": ")[1].split(", ")
        x, y = (int(prize[0][2:]) + 10000000000000, int(prize[1][2:]) + 10000000000000)

        a_presses = (b[0] * y - b[1] * x) / (b[0] * a[1] - b[1] * a[0])
        b_presses = (x - (a[0]) * a_presses) / b[0]

        if math.floor(a_presses) == a_presses and math.floor(b_presses) == b_presses:
            res += 3 * a_presses + b_presses
    
    print(int(res))
        

part2()