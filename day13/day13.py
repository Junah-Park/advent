def main():
    input = [[]]
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                input.append([])
            else:
                input[-1].append(line.strip())

    total = 0
    def hasHorizontal(pattern):
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[i-1]:
                j, k = i-2, i+1
                mirror = True
                while j>=0 and k<len(pattern):
                    if pattern[j] != pattern[k]:
                        mirror = False
                        break
                    j-=1
                    k+=1
                if mirror:
                    return i
        return -1

    def isLineMirror(line, j, k):
        mirror = True
        while j>=0 and k<len(line):
            if line[j] != line[k]:
                mirror = False
                break
            j-=1
            k+=1
        return mirror
    
    def hasVertical(pattern):
        for col in range(1, len(pattern[0])):
            if pattern[0][col] == pattern[0][col-1]:
                mirror = True
                for line in pattern:
                    if not isLineMirror(line, col-1, col):
                        mirror = False
                        break
                if mirror:
                    return col
            print(f'vertical miss: {pattern}')
        return 0

    for pattern in input:
        print(pattern)
        horizontal = hasHorizontal(pattern)
        if horizontal == -1:
            total += hasVertical(pattern)
        else:
            total += horizontal * 100
        
    print(total)

if __name__ == "__main__":
    main()
    