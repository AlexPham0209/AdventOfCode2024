from collections import defaultdict

def part1():
    res = 0
    adj = defaultdict(set)
    orders = []

    with open("day5.in") as file:
        rules, ordering = file.read().split("\n\n")

        for line in rules.split("\n"):
            a, b = map(int, line.split("|"))
            adj[b].add(a)
        
        for line in ordering.split("\n"):
            orders.append(list(map(int, line.split(","))))

    for order in orders:
        is_valid = True

        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                if order[j] in adj[order[i]]:
                    is_valid = False
                    break

        if is_valid:
            res += order[len(order)//2]

    print(res)

def part2():
    res = 0
    adj = defaultdict(set)
    orders = []

    with open("day5.in") as file:
        rules, ordering = file.read().split("\n\n")

        for line in rules.split("\n"):
            a, b = map(int, line.split("|"))
            adj[b].add(a)
        
        for line in ordering.split("\n"):
            orders.append(list(map(int, line.split(","))))

    for order in orders:
        is_valid = True

        for i in range(len(order)):
            for j in range(i + 1, len(order)):
                if order[j] in adj[order[i]]:
                    is_valid = False
                    temp = order[j]
                    order.pop(j)
                    order.insert(i, temp)
        
        if not is_valid:
            res += order[len(order)//2]
    print(res)
            
part2()