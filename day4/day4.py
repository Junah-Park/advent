# day 4 of advent

# read lines from input.txt
class Points:
    def __init__(self, amount=0):
        self.amount = amount
    def get(self):
        return self.amount
    def increase(self):
        if not self.amount:
            self.amount = 1
        else:
            self.amount *= 2

def main():

    with open('input.txt') as f:
        total = 0
        copies = {}
        for line in f:
            winningSet = set()
            points = 0
            line = line.strip()
            line = line.split(":")
            card = int(line.split(" ")[1])
            line = line[1]
            line = line.split("|")
            winning, hand = line[0], line[1]
            
            winning = [s for s in winning.split(" ") if s]
            hand = [s for s in hand.split(" ") if s]

            for num in winning:
                winningSet.add(num)
            for num in hand:
                if num in winningSet:
                    points+=1
            for i in range(points):
                copies[card+i] = copies.get(card+1, 0) + 1
            

            # iterate through winning and add to set until '|' is encountered
            # check if number in winning, increase amount if found
            print(line)
        print(total)

if __name__ == "__main__":
    main()
    