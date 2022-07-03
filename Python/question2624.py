#동전 바꿔주기, 골드 5
import sys


def coins_dp(n, k):
    global dp, T
    for i in range(T, 0, -1):
        for j in range(1, k+1):
            if i - (n*j) >= 0:
                dp[i] += dp[i - (n*j)]


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    dp = [0 for i in range(10001)]
    # coins_dp[x][n]
    # x원을 동전 n개까지 사용하여 교환할 때의 경우의 수
    dp[0] = 1
    for i in range(K):
        n, k = map(int, sys.stdin.readline().split())
        coins_dp(n, k)

    # print(dp)
    print(dp[T])