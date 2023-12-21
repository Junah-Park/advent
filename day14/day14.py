def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(list(line.strip()))
    # move all rocks north
    # starting from top, move rock up while empty above
    def rollNorth(row, col):
        while row > 0 and input[row-1][col] == '.':
            input[row][col], input[row-1][col] = input[row-1][col], input[row][col]
            row -= 1
    def rollWest(row, col):
        while col > 0 and input[row][col-1] == '.':
            input[row][col], input[row][col-1] = input[row][col-1], input[row][col]
            col -= 1
        
    def rollSouth(row, col):
        while row < len(input)-1 and input[row+1][col] == '.':
            input[row][col], input[row+1][col] = input[row+1][col], input[row][col]
            row += 1
        
    def rollEast(row, col):
        while col < len(input[row])-1 and input[row][col+1] == '.':
            input[row][col+1], input[row][col] = input[row][col], input[row][col+1]
            col += 1
        
    # calculate load    
    def calcLoad():
        total = 0
        for i, line in enumerate(input):
            for c in line:
                total += (len(input) - i) if c == 'O' else 0
        
        return total
    
    def cycle():
        for row in range(len(input)):
            for col, c in enumerate(input[row]):
                if c == 'O':
                    rollNorth(row, col)

        for col in range(len(input[0])):
            for row in range(len(input)):
                if input[row][col] == 'O':
                    rollWest(row, col)

        for row in range(len(input)-1, -1, -1):
            for col, c in enumerate(input[row]):
                if c == 'O':
                    rollSouth(row, col)

        for col in range(len(input[0])-1, -1, -1):
            for row in range(len(input)):
                if input[row][col] == 'O':
                    rollEast(row, col)
        return calcLoad()

    northLoad = -1
    prevLoad = cycle()

    #while northLoad != prevLoad:
    for i in range(1000000000):
        northLoad = prevLoad
        prevLoad = cycle()
    print(northLoad)

if __name__ == "__main__":
    main()
    