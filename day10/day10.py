def main():
    input = []
    sRow, row = 0, 0
    sCol = 0
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip())
            for col, c in enumerate(line):
                print(f'c: {c}')
                if c == 'S':
                    sRow = row
                    sCol = col            
            row += 1
    visited = set([(sRow, sCol)])
    from collections import deque
    q = deque()
    print(f'sRow: {sRow}')
    print(f'sCol: {sCol}')
    if sRow != 0 and (input[sRow-1][sCol] == '|' or input[sRow-1][sCol] == '7' or input[sRow-1][sCol] == 'F'):
        q.append((sRow-1, sCol, 1))
    if sCol != 0 and (input[sRow][sCol-1] == '-' or input[sRow][sCol-1] == 'L' or input[sRow][sCol-1] == 'F'):
        q.append((sRow, sCol-1, 1))
    if sCol < len(input[sRow]) - 1 and (input[sRow][sCol+1] == '-' or input[sRow][sCol+1] == '7' or input[sRow][sCol+1] == 'J'):
        q.append((sRow, sCol+1, 1))
    if sRow < len(input) - 1 and (input[sRow+1][sCol] == '|' or input[sRow+1][sCol] == 'L' or input[sRow+1][sCol] == 'J'):
        q.append((sRow+1, sCol, 1))
    maxSteps = 0

    tiles = {
        '|': [(1,0), (-1,0)], 
        '-': [(0,1), (0,-1)], 
        'L':[(-1,0), (0,1)], 
        'J':[(-1,0), (0,-1)], 
        '7':[(0,-1), (1,0)],
        'F':[(0,1), (1,0)],
        '.':[],
        }
    
    while q:
        curRow, curCol, curSteps = q.popleft()
        if  (curRow, curCol) in visited or curRow >= len(input) or curRow < 0 or curCol >= len(input[curRow]) or curCol < 0:
            continue
        maxSteps = max(maxSteps, curSteps)
        visited.add((curRow, curCol))
        for rowDiff, colDiff in tiles[input[curRow][curCol]]:
            q.append((curRow+rowDiff, curCol+colDiff, curSteps+1))

    print(maxSteps)

if __name__ == "__main__":
    main()
    