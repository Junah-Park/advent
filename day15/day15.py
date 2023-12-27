from functools import reduce
def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip())
    steps = input[0].strip().split(',')
    values = []
    for step in steps:
        value = 0
        for c in step:
            value += ord(c)
            value *= 17
            value %= 256
        values.append(value)
    print(steps)
    print(values)
    total = sum(values)
    print(total)
            
if __name__ == "__main__":
    main()
    