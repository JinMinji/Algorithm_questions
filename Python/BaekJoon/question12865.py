# 12865, 평범한 배낭, 골드5
import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    weights = []
    values = []

    for i in range(N):
        w, v = map(int, sys.stdin.readline().split())
        weights.append(w)
        values.append(v)

    # K만큼의 체력으로 N섬을 들렀을 때 최대로 구할 수 있는 사람 수, 현재까지의 체력소모합
    dp = [[[0, 0] for i in range(K+1)] for i in range(N+1)]

    for i in range(N+1):
        for a in range(K+1):
            if i == 0 or a == 0:
                dp[i][a] = 0
            elif weights[i-1] <= a:    # i번째 섬을 들를 수 있을 때
                # i번째 섬까지 고려할 때
                # a의 체력으로 방문할 때 구할 수 있는 최대사람 수는
                # i번째 섬을 방문하지 않았을 때의 최대사람수
                # vs i번째섬을 방문하고, a-monster[i]의 체력으로 방문할 수 있는 최대 사람수의 합
                dp[i][a] = max(values[i-1] + dp[i-1][a-weights[i-1]], dp[i-1][a])

            else:
                dp[i][a] = dp[i-1][a]

    # print()
    # for i in range(len(dp)):
    #     print(*dp[i])

    print(dp[N][K])