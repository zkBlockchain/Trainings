def main():
    """ The Hoss 2 DP task
    Input - N x M (chess board)
    Finding count of ways from (0, 0) to (N, M)
   
    Condition: 
        * Move the hoss down by two and to the right by one
        * Move the hoss down by one and to the right by two
        * Move the hoss down by two and to the left by one
        * Move the hoss top by one and to the right by two
    """
    N, M = [int(x) for x in input().split()]
    DP = [[0] * M for x in range(N)]
    DP[0][0] = 1
    
    for D in range(N+M):
        for i in range(N):
            j = D - i
            if j < 0 or j >= M: continue

            if not (i - 2 < 0 or j - 1 < 0):
                DP[i][j] += DP[i-2][j-1]
            if not (i - 1 < 0 or j - 2 < 0):
                DP[i][j] += DP[i-1][j-2]
            if not (i - 2 < 0 or j + 1 >= M):
                DP[i][j] += DP[i-2][j+1]
            if not (i + 1 >= N or j - 2 < 0):
                DP[i][j] += DP[i+1][j-2]

    print(DP[-1][-1])


if __name__ == '__main__':
    main()
