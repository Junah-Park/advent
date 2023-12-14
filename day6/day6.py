def main():
    # t=d/x+x
    input = []
    time = []
    distance = []
    with open('input.txt') as f:
        for line in f:
            if line[0] == 'T':
                for num in line.strip().split(':')[1].strip().split(' '):
                    if num != '':
                        time.append(int(num))
            if line[0] == 'D':    
                for num in line.strip().split(':')[1].strip().split(' '):
                    if num != '':
                        distance.append(int(num))

    ways = []
    for time, distance in zip(time, distance):
        count = 0
        for t in range(time):
            if (time - t) * t > distance:
                count += 1
        ways.append(count)

    product = 1

    for way in ways:
        product *= way
    print(product)

if __name__ == "__main__":
    main()
    