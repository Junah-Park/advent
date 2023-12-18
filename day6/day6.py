def main():
    # t=d/x+x
    input = []
    time = ''
    distance = ''
    with open('input.txt') as f:
        for line in f:
            if line[0] == 'T':
                for num in line.strip().split(':')[1].strip().split(' '):
                    if num != '':
                        time += num
                time = int(time)
            if line[0] == 'D':
                    
                for num in line.strip().split(':')[1].strip().split(' '):
                    if num != '':
                        distance += num
                distance = int(distance)


    def distanceOf(t):
        return (time-t) * t
    solutionLeft = 0
    l, r = 1, time
    while True:
        m = (l+r)//2
        n = m+1
        print(m)
        if distanceOf(m) < distance and distanceOf(n) > distance:
            solutionLeft = n
            break
        elif distanceOf(m) < distance:
            l = m+1
        else:
            r = m-1
    
    solutionRight = 0
    l, r = solutionLeft, time
    while True:
        m = (l+r)//2
        n = m-1
        print(m)
        if distanceOf(m) <= distance and distanceOf(n) > distance:
            solutionRight = n
            break
        elif distanceOf(m) < distance:
            r = m-1
        else:
            l = m+1
    print(f'solutionRight: {solutionRight}')
    print(f'solutionLeft: {solutionLeft}')
    print(solutionRight - solutionLeft + 1)


    # ways = []
    # for time, distance in zip(time, distance):
    #     count = 0
    #     for t in range(time):
    #         if (time - t) * t > distance:
    #             count += 1
    #     ways.append(count)

    # product = 1

    # for way in ways:
    #     product *= way
    # print(product)

if __name__ == "__main__":
    main()
    