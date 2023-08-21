#자두나무, 골드5
import sys


def dp_solution():
    global dp, orders, T, W

    for i in range(1, T):
        if orders[i] == 1:
            for cnt in range(W + 1):
                if cnt == 0:
                    dp[i][cnt] = dp[i-1][cnt] + 1
                elif cnt % 2 == 0:    # 현재 자두의 위치가 1
                    dp[i][cnt] = max(dp[i-1][cnt-1] + 1, dp[i-1][cnt] + 1)
                else:   #현재 자두의 위치는 2
                    dp[i][cnt] = max(dp[i-1][cnt-1], dp[i-1][cnt])

        else:
            for cnt in range(1, W + 1):
                if cnt == 0:
                    dp[i][cnt] = dp[i - 1][cnt]
                elif cnt % 2 == 0:  # 현재 자두의 위치가 1
                    dp[i][cnt] = max(dp[i - 1][cnt - 1], dp[i - 1][cnt])

                else:  # 현재 자두의 위치는 2`
                    dp[i][cnt] = max(dp[i - 1][cnt - 1] + 1, dp[i - 1][cnt] + 1)


if __name__ == "__main__":
    T, W = map(int, sys.stdin.readline().split())

    orders = list()
    for i in range(T):
        orders.append(int(sys.stdin.readline()))

    # W는 30,, 0~30번 까지 이동횟수,,,
    dp = [[0 for i in range(W+1)] for i in range(T)]
    #dp[T][cnt] 타임 T+1에서 cnt번 이동했을 때 최대 개수

    if orders[0] == 1:
        for cnt in range(W + 1):
            if cnt % 2 == 0:
                dp[0][cnt] = 1
            else:
                dp[0][cnt] = 0
    else:
        for cnt in range(W + 1):
            if cnt % 2 == 0:
                dp[0][cnt] = 0
            else:
                dp[0][cnt] = 1

    dp_solution()

    # for i in range(T):
    #     print(dp[i])
    print(max(dp[T-1]))



