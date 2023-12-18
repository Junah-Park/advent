# take a step back
# refactor as we go
def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line)
    total = 0
    def makeSeq(seq):
        #print('makeSeq call')
        all0s = False
        seqStarts = [seq[0]]
        while not all0s:
            differences = []
            for i in range(1, len(seq)):
                diff = seq[i] - seq[i-1]
                differences.append(diff)
            for diff in differences:
                all0s = True
                if diff != 0:
                    all0s = False
        # save the ends of the sequences for final prediction
        # seq becomes the next level of the pyramid (differences)
            #print(f'differences: {differences}')
            seqStarts.append(differences[0])
            seq = differences
        #print(f'sequence starts: {seqStarts}')
        return predictSeq(seqStarts)

    def predictSeq(seqStarts):
        diff = 0
        seqStarts.reverse()
        #print(f'seqStarts: {seqStarts}')
        for start in seqStarts:
            diff = start - diff
            #print(f'diff: {diff}')
        return diff

    for seq in input:
        seq = [int(x) for x in seq.strip().split(' ')]
        #print(f'sequence: {seq}')
        total += makeSeq(seq)
    print(total)

if __name__ == "__main__":
    main()
    