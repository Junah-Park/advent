import math
def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line)
    steps = input[0].strip()
    netMap = {}
    curNodes = []
    Zs = set()
    for line in input[2:]:
        values = line.strip().split('=')
        key = values[0].strip()
        if key[-1] == 'A':
            curNodes.append(key)
        if key[-1] == 'Z':
            Zs.add(key)
        values = values[1].strip().split(',')
        left = values[0][1:]
        right = values[1][1:4]
        netMap[key] = (left, right)
    
    visitedZs = [{}] * len(curNodes)
    cycleLengths = [None] * len(curNodes)
    count = 0
    # 1 2 3 
    # 1 2 3 4
    print(curNodes)
    print(Zs)
    def stepAll(step, count):
        allZs = True
        for i, node in enumerate(curNodes):
            if step == 'L':
                nextNode = netMap[node][0]
                if nextNode[-1] == 'Z':
                    cycleLengths[i] = count
                if nextNode[-1] != 'Z':
                    allZs = False
            else:
                nextNode = netMap[node][1]
                if nextNode[-1] == 'Z':
                    cycleLengths[i] = count
                if nextNode[-1] != 'Z':
                    allZs = False
            curNodes[i] = nextNode
        return allZs

    while True:
        for step in steps:
            count += 1
            if stepAll(step, count):
                print(count)
                return
            lcm = True
            for cycleLength in cycleLengths:
                if not cycleLength:
                    lcm = False
                    break
            if lcm:
                lcm = math.lcm(*cycleLengths)
                print(lcm)
                return
        
if __name__ == "__main__":
    main()
    