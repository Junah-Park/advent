# start a basic python script
# read a file called input.txt and iterate over each line
def main():
    schematic = []
    with open('input.txt') as f:
        for line in f:
            print(line)
            schematic.append(line.strip())
    print(schematic)
    # iterate through each char, search all 8 positions around it
    # O8*row*col
    # bool that represents whether current number is confirmed
    # when we encounter a ".", if confirmed, then add the number to total
    # reset confirmed and curNum

    # list of every "*" coordinate
    # hashmap of every digit coordinate: number
    # infer which spaces map to number using curNum length
    # at the end, loop through every "*" to look for number
    sum = 0
    curNum = ""
    confirmed = False
    numMap = {}
    gears = []
    id = 1
    ratioSum = 0

    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if not schematic[row][col].isdigit():
                if schematic[row][col] == "*":
                    gears.append((row,col))
                if confirmed:
                    if curNum:
                        sum += int(curNum)
                for subCol in range(col-len(curNum), col):
                    numMap[(row,subCol)] = ( int(curNum), id )
                id += 1
                confirmed = False
                curNum = ""
                continue
            if schematic[row][col].isdigit():
                curNum += schematic[row][col]
                # search around for symbol
                for subRow in range(row-1, row+2):
                    for subCol in range(col-1, col+2):
                        if subRow >= 0 and subCol >= 0 and subRow < len(schematic) and subCol < len(schematic[subRow]):
                            if not schematic[subRow][subCol].isdigit() and not schematic[subRow][subCol] == ".":
                                confirmed = True
        if confirmed and curNum:
            sum += int(curNum)
        confirmed = False
        curNum = ""
    for row,col in gears:
        ratio = 1
        visitedIds = set()
        for subRow in range(row-1, row+2):
            for subCol in range(col-1, col+2):
                if subRow >= 0 and subCol >= 0 and subRow < len(schematic) and subCol < len(schematic[subRow]):
                    if (subRow, subCol) in numMap:
                        if not numMap[(subRow, subCol)][1] in visitedIds:
                            visitedIds.add(numMap[(subRow, subCol)][1])
                            ratio *= numMap[(subRow, subCol)][0]
        if len(visitedIds) < 2:
            continue
        else:
            ratioSum += ratio

    print(sum)
    print(ratioSum)
    return 0

if __name__ == "__main__":
    main()