def main():
    """ Max cost way & price
        First input - N x M
        Next lines are a table
        Each table cell is a cost
        Move either right or down
        Target - bottom right cell
        The task is to find the max cost way & price
    """
    array = []
    N, M = ([int(x) for x in input().split()])
    for _ in range(N):
        array.append([int(x) for x in input().split()])

    bottom, right = 0, 0
    for i in range(N):
        for j in range(M):
            if i >= 1 and j >= 0: 
                bottom = array[i-1][j]
            if i >= 0 and j >= 1: 
                right = array[i][j-1]
            array[i][j] += max(bottom, right)
            bottom, right = 0, 0
            
    way = []
    i, j = N - 1, M - 1
    while i != 0 or j != 0:
        if i >= 1 and j >= 1:
            if array[i-1][j] >= array[i][j-1]:
                way.append('D')
                i -= 1
            else:
                way.append('R')
                j -= 1
        else:
            if i >= 1:
                way.append('D')
                i -= 1
            else:
                way.append('R')
                j -= 1

    way.reverse()
    print(array[-1][-1])
    print(*way)


if __name__ == '__main__':
    main()
