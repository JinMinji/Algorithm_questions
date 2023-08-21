# 저울, 골드 3

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    INF = 10**5
    compare = [[0 for i in range(N+1)] for i in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        compare[a][b] = 1

    for i in range(N+1):
        compare[i][i] = 1

    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if compare[i][k] and compare[k][j]:
                    compare[i][j] = 1

    for i in range(1, N+1):
        cnt = 0
        for j in range(1, N+1):
            if not compare[i][j] and not compare[j][i]:
                cnt += 1

        print(cnt)

