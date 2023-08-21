# 행렬 곱셈 순서

dp = list()

if __name__ == '__main__':
    N = int(input())

    arr_size = list()

    for i in range(N):
        arr_size.append(list(map(int, input().split(' '))))

    max_val = 1024*1024*1024

    dp = [[0 for _ in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                dp[i][j] = 0

            elif i + 1 == j:    #
                dp[i][j] = arr_size[i][0]*arr_size[i][1]*arr_size[j][1]

            else:
                dp[i][j] = max_val      # 최댓값 넣어두고, min
                for m in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j] + arr_size[i][0] * arr_size[m][1] * arr_size[j][1])

    print(dp[0][N-1])