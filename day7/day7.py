from collections import defaultdict
def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line)
    fives, fours, houses, threes, twoPairs, pairs, highs = [], [], [], [], [], [], []
    faceCard = {'T':10, 'J': 1, 'Q': 12, 'K':13, 'A': 14}

    def addType(hand, bid):
        cardCount = defaultdict(int)
        jCount = 0
        for i, card in enumerate(hand):
            if card == 'J':
                jCount += 1
            else:
                cardCount[card] += 1
            if not card.isdigit():
                hand[i] = faceCard[card]
            hand[i] = int(hand[i])

        type = list(cardCount.values())
        type.sort(reverse=True)
        if jCount == 5:
            type.append(5)
        else:
            for i in range(jCount):
                if type[0] < 5:
                    type[0] += 1
                else:
                    type[1] += 1

        if type[0] == 5:
            fives.append(hand + [bid])
        elif type[0] == 4:
            fours.append(hand + [bid])
        elif type[0] == 3 and type[1] == 2:
            houses.append(hand + [bid])
        elif type[0] == 3:
            threes.append(hand + [bid])
        elif type[0] == 2 and type[1] == 2:
            twoPairs.append(hand + [bid])
        elif type[0] == 2:
            pairs.append(hand + [bid])
        else:
            highs.append(hand + [bid])
        
    for line in input:
        temp = line.strip().split(' ')
        hand = [x for x in temp[0] if x != '']
        bid = int(temp[1])
        addType(hand, bid)

    # sort each bucket
    hands = []
    for bucket in [highs, pairs, twoPairs, threes, houses, fours, fives]:
        bucket.sort()
        hands += bucket
    # merge buckets

    # calc total winnings
    total = 0
    for rank, hand in enumerate(hands):
        total += (rank + 1) * hand[-1]
    print(total)


if __name__ == "__main__":
    main()
    