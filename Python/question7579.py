#20210609 앱

def min_cost():
    for i in range(1, N+1):
        for j in range(1, M+1):
            if app_memory[i-1] < j:
                min_dp[i][j] = min_dp[i-1][j]
            else:
                min_dp[i][j] = min(app_cost[i-1]+min_dp[i-1][j-app_memory[i]], min_dp[i-1][j])

if __name__ == '__main__':
    N, M = map(int, input().split())

    app_memory = list(map(int, input().split()))
    app_cost = list(map(int, input().split()))

    MAX_cost = 10000
    min_dp = [[MAX_cost for i in range(M+1)]for j in range(N+1)]
    # min_dp[N][M]
    # N개의 앱을 종료하여 M메모리를 확보할 때의 Min cost

    min_cost()
    answer = MAX_cost
    for i in range(N):
        answer = min(min_dp[i][M], answer)

    print(answer)

