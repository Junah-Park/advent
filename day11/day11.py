def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip())
    
    # for each galaxy we need only bfs outward, mapping each encountered galaxy on the way with the path
    # how to expand the universe? representational by adding a row or column index or actually fill a whole row/col?
    # filling an empty may be too computationally intense.
    # create a set of galaxyrows and galaxycols, loop through and that will find empties
    # coordinates for all the galaxies then become incorrect. Could we adjust?
    # perhaps just add an additional step when an 'empty row' or 'empty col' is found
    emptyRows = [999999 for i in range(len(input))]
    emptyCols = [999999 for i in range(len(input[0]))]
    galaxies = []
    for row, line in enumerate(input):
        for col, c in enumerate(line):
            if c == '#':
                emptyRows[row] = 0
                emptyCols[col] = 0
                galaxies.append([row,col])

    total = 0
    galaCount = 0
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            galaxy1 = galaxies[i]
            galaxy2 = galaxies[j]
            total += abs(galaxy2[0] - galaxy1[0])
            total += abs(galaxy2[1] - galaxy1[1])
            row1 = min(galaxy1[0], galaxy2[0])
            row2 = max(galaxy1[0], galaxy2[0])
            col1 = min(galaxy1[1], galaxy2[1])
            col2 = max(galaxy1[1], galaxy2[1])
            total += sum(emptyRows[row1:row2])
            total += sum(emptyCols[col1:col2])
            galaCount += 1


    
if __name__ == "__main__":
    main()
    