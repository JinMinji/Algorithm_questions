#2579, 계단 오르기, 실버 3


if __name__ == "__main__":
    N = int(input())

    stairs = list()
    for i in range(N):
        stairs.append(int(input()))

    dp =[[0, 0] for i in range(N+1)]
    # 현재 계단을 밟았을 때, 밟지 않았을 때

    dp[1] = [stairs[0], 0]

    for i in range(2, N+1):
        # 앞에서 2칸 뛰었을때 최대
        dp[i][0] = max(dp[i-2]) + stairs[i-1]

        # 앞에서 1칸 뛰었을때 최대
        dp[i][1] = dp[i-1][0] + stairs[i-1]
    #
    # for i in range(N+1):
    #     print(*dp[i])

    print(max(dp[N]))
