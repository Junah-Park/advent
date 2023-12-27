from collections import deque

def main():
    input = []
    with open('input.txt') as file:
        for line in file:
            input.append(line.strip())

    visited = [[set() for _ in range(len(input[0]))] for _ in range(len(input))]

    def bfs(start_row, start_col, start_direction):
        queue = deque([(start_row, start_col, start_direction)])

        while queue:
            row, col, direction = queue.popleft()
            
            if row < 0 or row >= len(input) or col < 0 or col >= len(input[0]):
                continue
            if direction in visited[row][col]:
                continue

            visited[row][col].add(direction)

            space = input[row][col]

            if space == '|':
                if direction in ['>', '<']:
                    queue.append((row-1, col, '^'))
                    queue.append((row+1, col, 'v'))
                elif direction == '^':
                    queue.append((row-1, col, direction))
                else:
                    queue.append((row+1, col, direction))

            elif space == '-':
                if direction in ['^', 'v']:
                    queue.append((row, col-1, '<'))
                    queue.append((row, col+1, '>'))
                elif direction == '>':
                    queue.append((row, col+1, direction))
                else:
                    queue.append((row, col-1, direction))

            elif space == '/':
                if direction == '>':
                    queue.append((row-1, col, '^'))
                elif direction == 'v':
                    queue.append((row, col-1, '<'))
                elif direction == '<':
                    queue.append((row+1, col, 'v'))
                else:
                    queue.append((row, col+1, '>'))

            elif space == '\\':
                if direction == '>':
                    queue.append((row+1, col, 'v'))
                elif direction == 'v':
                    queue.append((row, col+1, '>'))
                elif direction == '<':
                    queue.append((row-1, col, '^'))
                else:
                    queue.append((row, col-1, '<'))

            else:
                if direction == '>':
                    queue.append((row, col+1, direction))
                if direction == 'v':
                    queue.append((row+1, col, direction))
                if direction == '<':
                    queue.append((row, col-1, direction))
                if direction == '^':
                    queue.append((row-1, col, direction))

    bfs(0, 0, '>')

    sum = 0
    for line in visited:
        for c in line:
            if c:
                sum += 1
    print(sum)

if __name__ == "__main__":
    main()
