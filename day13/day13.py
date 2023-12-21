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
            smudge = 1
            j, k = i-1, i
            mirror = True
            while j>=0 and k<len(pattern):
                for col in range(len(pattern[k])):
                    if pattern[j][col]!=pattern[k][col]:
                        if smudge:
                            smudge -= 1
                        else:
                            mirror = False
                            break
                if not mirror:
                    break
                j-=1
                k+=1
            if mirror and not smudge:
                return i
        return -1

    def isLineMirror(line, j, k, smudge):
        mirror = True
        while j>=0 and k<len(line):
            if line[j] != line[k]:
                if not smudge:
                    mirror = False
                    break
                else:
                    smudge-=1
            j-=1
            k+=1
        return mirror, smudge
    
    def hasVertical(pattern):
        for col in range(1, len(pattern[0])):
            smudge = 1
            if pattern[0][col] == pattern[0][col-1]:
                mirror = True
                for line in pattern:
                    mirror, smudge = isLineMirror(line, col-1, col, smudge)
                    if not mirror:
                        break
                if mirror and not smudge:
                    return col
        return 0

    for pattern in input:
        horizontal = hasHorizontal(pattern)
        if horizontal == -1:
            total += hasVertical(pattern)
        else:
            total += horizontal * 100
        
    print(total)

if __name__ == "__main__":
    main()
    