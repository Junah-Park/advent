def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line)
    steps = input[0].strip()
    print(steps)
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
    
    count = 0
    curKey = 'AAA'
    while curKey != 'ZZZ':
        for step in steps:
            if step == 'L':
                curKey = netMap[curKey][0]
            else:
                curKey = netMap[curKey][1]
            count += 1
            if curKey == 'ZZZ':
                print(count)
                return count
    return count
        
if __name__ == "__main__":
    main()
    