#11052, 카드 구매하기, 실버1


if __name__ == "__main__":
    N = int(input())
    cards = list(map(int, input().split()))

    dp = [[0 for i in range(N+1)] for i in range(N)]

    dp[0] = [cards[0]*i for i in range(N+1)]

    for i in range(1, N):
        for j in range(i+1):
            dp[i][j] = dp[i - 1][j]
        for j in range(i+1, N+1):
            # print(i, j-i-1)
            dp[i][j] = max(dp[i-1][j], dp[i][j-i-1] + cards[i])

    # for i in range(N):
    #     print(*dp[i])

    print(dp[N-1][N])