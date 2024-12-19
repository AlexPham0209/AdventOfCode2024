def part1():
    with open("day9.in") as file:
        for line in file:
            disk = []
            id = 0
            for i in range(0, len(line) - 1, 2):
                for j in range(int(line[i])):
                    disk.append(str(i//2))
                
                for j in range(int(line[i + 1])):
                    disk.append(".")
            
            if len(line) % 2 != 0:
                for i in range(int(line[-1])):
                    disk.append(str(len(line)//2))

            l = 0
            r = len(disk) - 1

            while l < r:
                if disk[l] != ".":
                    l += 1
                elif disk[r] == ".":
                    r -= 1
                else:
                    temp = disk[r]
                    disk[r] = disk[l]
                    disk[l] = temp

            res = 0
            for i in range(len(disk)):
                if disk[i] == ".":
                    break
                res += i * int(disk[i])
            print(res)


def part2():
    with open("day9.in") as file:
        for line in file:
            disk = []
            id = 0
        
            for i in range(0, len(line) - 1, 2):
                for j in range(int(line[i])):
                    disk.append(str(i//2))
                
                for j in range(int(line[i + 1])):
                    disk.append(".")

            if len(line) % 2 != 0:
                for i in range(int(line[-1])):
                    disk.append(str(len(line)//2))

            blocks = dict()

            l = -1
            for i in range(len(disk) - 1):
                if disk[i] == ".":
                    continue
            
                if l == -1:
                    l = i
                
                if disk[i] != disk[i + 1]:
                    blocks[int(disk[i])] = (l, i)
                    l = -1

            blocks[int(disk[-1])] = (l, len(disk) - 1)

            id = len(line)//2
            for i in range(len(line)//2, -1, -1):
                l, r = blocks[i]
                j = 0
                while j < l:
                    if disk[j] != ".":
                        j += 1 
                        continue
                    
                    k = j
                    while k < l and disk[k] == ".":
                        k += 1

                    total = r - l + 1

                    if total > k - j:
                        j = k
                        continue
                    
                    while j < l and r >= l:
                        temp = disk[r]
                        disk[r] = disk[j]
                        disk[j] = temp
                        r -= 1
                        j += 1
                    break

            res = 0
            for i in range(len(disk)):
                if disk[i] == ".":
                    continue
                res += i * int(disk[i])
            
            print(res)

part2()