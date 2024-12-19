def part1():
    patterns, towels = open("day19.in").read().split("\n\n")

    patterns = set(patterns.split(", "))
    towels = towels.split("\n")
    res = 0

    for towel in towels:
        dp = [False] * (len(towel) + 1)

        dp[0] = True
        for i in range(1, len(dp)):
            for pattern in patterns:
                if towel[i - len(pattern) : i] != pattern:
                    continue

                if i >= len(pattern) and dp[i - len(pattern)]: 
                    dp[i] = True
        
        if dp[-1]:
            res += 1 

    print(res)


def part2():
    patterns, towels = open("day19.in").read().split("\n\n")

    patterns = set(patterns.split(", "))
    towels = towels.split("\n")
    res = 0

    for towel in towels:
        dp = [False] * (len(towel) + 1)

        dp[0] = 1
        for i in range(1, len(dp)):
            for pattern in patterns:
                if towel[i - len(pattern) : i] != pattern:
                    continue

                if i >= len(pattern) and dp[i - len(pattern)]: 
                    dp[i] += dp[i - len(pattern)]
        
        res += dp[-1]

    print(res)

        
part2()