# 소형기관차 골드 4


if __name__ == '__main__':
    N = int(input())
    trains = list(map(int, input().split(' ')))
    M = int(input())

    dp = [[0 for i in range(len(trains)+1)] for i in range(4)]

    # 누적합 담아놓을 배열
    totals = [0 for i in range(len(trains)+1)]

    cur_total = sum(trains[:M])
    totals[M] = cur_total
    dp[1][M] = cur_total

    for n in range(M + 1, len(trains)+1):
        cur_total -= trains[n - M - 1]
        cur_total += trains[n - 1]
        totals[n] = cur_total
        # dp[1][n] n번째 기차까지 봤을 때, 객차 1개로 수송할 수 있는 최대 승객 수
        dp[1][n] = max(dp[1][n - 1], cur_total)

    for n in range(2*M, len(trains)+1):
        # dp[2][n] n번째 기차까지 봤을 때, 객차 2개로 수송할 수 있는 최대 승객 수
        for k in range(M, n-M+1):   # 1번째 객차와 2번째 객차 사이를 나누는 k
            dp[2][n] = max((dp[1][k] + max(totals[k+M:n+1])), dp[2][n])

    for n in range(3*M, len(trains)+1):
        # dp[3][n] n번째 기차까지 봤을 때, 객차 3개로 수송할 수 있는 최대 승객 수
        for k in range(2*M, n-M+1):  # 2번째 객차와 3번째 객차 사이를 나누는 k
            dp[3][n] = max((dp[2][k] + max(totals[k+M:n+1])), dp[3][n])

    print(dp[3][N])
