# 파일 합치기 3

max_val = 10000
dp = list()
files = list()


def dp_make(x, y):
    if dp[x][y] != max_val:
        return dp[x][y]

    elif x == y:    # 범위가 한개일때
        dp[x][y] = 0

    elif x + 1 == y:    # 바로 옆에 붙어있을 때
        dp[x][y] = files[x] + files[y]

    else:
        for m in range(x, y):
            dp[x][y] = min(dp[x][y], dp_make(x, m) + dp_make(m+1, y))

    return dp[x][y]


if __name__ == '__main__':
    T = int(input())

    result = list()

    for t in range(T):
        K = int(input())

        files = list(map(int, input().split(" ")))

        max_val = 10000 * K
        dp = [[max_val for _ in range(K)] for _ in range(K)]

        result.append(dp_make(0, K-1))
        for i in range(len(dp)):
            print(dp[i])

    for i in range(len(result)):
        print(result[i])