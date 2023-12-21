def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip())
    
    total = 0



    # line and arr are subarrays
    # when damaged encountered, decrement arr[0]
    # base case: line is empty and arr is empty
    # failing cases: 
    # damaged, but none left in arr[0]
    # operational, but still some in arr[0]
    # whenever ? is encountered, 
    # #: recursive call with arr-=1
    # .: recursive call if sequence False or arr[0] == 0
    # flag for whether we're in a sequence

    # def dfs(line, arr, sequence):
    #     if not line:
    #         if arr:
    #             return 0
    #         else:
    #             return 1
    #     count = 0
    #     if sequence:
    #         if line[0] == '#':
    #             if arr[0] > 0:
    #                 arr[0] -= 1
    #                 count += dfs(line[1:])
    #             else:
    #                 return 0
    #         elif line[0] == '?':
    #             line[0] = '.'
    #             count += dfs(line, arr, sequence)
    #             line[0] = '#'
    #             count += dfs(line, arr, sequence)
    #         else:
    #             if arr[0] > 0:
    #                 return 0
    #             else:
    #                 arr[1:]
    #                 sequence = False
    #             count += dfs(line[1:], arr, sequence)
    #     else:
    #         if line[0] == '#':
    #             if not arr:
    #                 return 0
    #             sequence = True
    #             arr[0] -= 1
    #         else:
    #             count += dfs(line[1:], arr, sequence)
    #     return count

    # return list of all possible strings
    def findPossible(i, possibility):
        if i == len(possibility):
            possibilities.append(tuple(possibility))
        elif possibility[i] == '?':
            possibility[i] = '.'
            findPossible(i+1, possibility)
            possibility[i] = '#'
            findPossible(i+1, possibility)
            possibility[i] = '?'
        else:
            findPossible(i+1, possibility)
        return
            
        
    # validate whether string matches arrangement
    def validate(possibility, arr):
        # if we encounter a #, subtract from arr[0]. If arr is empty or arr[0] < 0 then fail
        # if we encounter a ., if arr[0]==0, popleft else continue
        # when we reach the end, if arr is empty then return 1
        sequence = False
        for c in possibility:
            if sequence:
                if c == '#':
                    if not arr or arr[0] <= 0:
                        return 0
                    else:
                        arr[0]-=1
                else:
                    if arr and arr[0] == 0:
                        arr = arr[1:]
                        sequence = False
                    else:
                        return 0
            else:
                if c == '#':
                    if not arr:
                        return 0
                    sequence = True
                    arr[0] -= 1
                else:
                    continue
        if not arr or (arr[0]==0 and len(arr)==1):
            return 1
        else:
            return 0

    for line in input:
        possibilities = []
        line = line.split(' ')
        arr = [int(x) for x in line[1].strip().split(',')]
        line = list(line[0].strip())
        findPossible(0, line)
        for possibility in possibilities:
            total += validate(possibility, arr.copy())
    print(total)

if __name__ == "__main__":
    main()
    