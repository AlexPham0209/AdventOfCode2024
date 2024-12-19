memory = []
pc = 0
a = 0
b = 0
c = 0
res = ""
f = open("day17.out", "w")

def step():
    global a, b, c, pc, memory
    # f.write(f"PC: {pc}\n")
    # f.write(f"I: {memory[pc]}\n")
    # f.write(f"A: {a}\n")
    # f.write(f"B: {b}\n")
    # f.write(f"C: {c}\n\n")
    #print(a)

    opcode = memory[pc]
    pc += 1 

    if pc < len(memory):
        execute(opcode)
        return True
    
    return False

def get_combo_op(val):
    global a, b, c
    match val:
        case 0 | 1 | 2 | 3:
            return val
        
        case 4:
            return a 
        
        case 5:
            return b
        
        case 6:
            return c
        
        case _:
            return 0

def execute(opcode):
    global pc, a, b, c, memory, res
    match opcode:
        case 0:
            a = a >> get_combo_op(memory[pc])
            pc += 1
        
        case 1:
            b ^= memory[pc]
            pc += 1 

        case 2:
            b = get_combo_op(memory[pc]) % 8
            pc += 1 

        case 3:
            if a != 0:
                pc = memory[pc]
            else:
                pc += 1

        case 4:
            b ^= c 
            pc += 1 

        case 5:
            combo = get_combo_op(memory[pc]) % 8
            res += str(combo) + ","
            pc += 1

        case 6:
            b = a >> get_combo_op(memory[pc])
            pc += 1

        case 7:
            c = a >> get_combo_op(memory[pc])
            pc += 1


def part1():
    global pc, a, b, c, memory, res
    regs, mem = open("day17.in").read().split("\n\n")
    a, b, c = map(int, [r[12:] for r in regs.split("\n")])
    
    a = 202425427831341
    memory = list(map(int, mem[9:].split(",")))

    f.write("fsadf\n")
    f.write(f"PC: {pc}\n")
    f.write(f"A: {a}\n")
    f.write(f"B: {b}\n")
    f.write(f"C: {c}\n")
    f.write(f"Memory: {memory}\n\n")
    
    while pc < len(memory):
        step()
    
    f.write(res[:-1] + "\n")
    f.write(''.join(res[:-1].split(",")) + "\n")
    f.write(f"PC: {pc}\n")
    f.write(f"A: {a}\n")
    f.write(f"B: {b}\n")
    f.write(f"C: {c}\n\n")


def solve(a, i, memory, solutions): 
    if i < 0:
        if output(a) == "2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0":
            solutions.append(a)
        return

    for j in range(8):
        temp = a << 3 | j
    
        if output(a << 3 | j) in "2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0":
            solve(a << 3 | j, i - 1, memory, solutions)
        

def output(a):
    res = ""
    b = 0
    c = 0
    while a != 0:
        b = a % 8
        b ^= 1
        c = a >> b 
        a >>= 3 
        b ^= 4
        b ^= c

        res += str(b % 8) + ","

    return res[:-1]

def part2():
    global pc, a, b, c, memory, total
    regs, mem = open("day17.in").read().split("\n\n")
    a, b, c = map(int, [r[12:] for r in regs.split("\n")])
    
    memory = list(map(int, mem[9:].split(",")))
    solutions = []
    solve(0, len(memory) - 1, memory, solutions)
    print(solutions[0])

part2()
#part1()

#print(output(202356708354602))