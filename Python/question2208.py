# 2208, 보석 줍기, 골드2
import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    # M~N개의 묶음 중, 가장 큰 값을 담은 것
    # dp[i][M] = i번째 인덱스까지 봤을 때, M개의 묶음 중 가장 큰 값

    dp = [[0 for i in range(N+1)] for i in range(N)]

    values = list()
    for i in range(N):
        values.append(int(sys.stdin.readline().rstrip()))

    tmp_total = sum(values[:M])
    # print(tmp_total)
    dp[M-1][M] = tmp_total
    for i in range(M, N):
        tmp_total += values[i]
        dp[i][i+1] = tmp_total

    for i in range(len(dp)):
        print(*dp[i])
    print()

    for i in range(M, N):
        for j in range(M, i+1):
            dp[i][j] = dp[i - 1][j] + values[i] - values[i - j]

    # for i in range(len(dp)):
    #     print(*dp[i])

    answer = max(dp[N-1])

    print(answer)