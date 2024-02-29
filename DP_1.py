def main():
    """ The cheapest way
        First input - N x M
        Next lines are a table
        Each table cell is a cost
        Move either right or down
        Target - bottom right cell
        The task is to find the cheapest way
    """
    array = []
    N, M = ([int(x) for x in input().split()])
    for _ in range(N):
        array.append([int(x) for x in input().split()])
    
    DP = [[0] * (M+1) for _ in range(N+1)]
    DP[1][1] = array[0][0]

    for i in range(N+1):
        DP[i][0] = float('inf')

    for i in range(M+1):
        DP[0][i] = float('inf')
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            if DP[i][j] == 0:
                DP[i][j] = array[i-1][j-1] + min(DP[i-1][j], DP[i][j-1])
    print(DP[-1][-1])


if __name__ == '__main__':
    main()


