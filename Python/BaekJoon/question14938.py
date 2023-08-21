#서강그라운드, 골드4
#누가봐도 플로이드와샬


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    #아이템 개수를 담은 배열
    items = list(map(int, input().split()))

    INF = 10**5
    ground = [[INF for i in range(n)] for i in range(n)]
    for i in range(n):
        ground[i][i] = 0

    for i in range(r):
        a, b, l = map(int, input().split())
        ground[a - 1][b - 1] = l
        ground[b - 1][a -1] = l

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if ground[i][j] > ground[i][k] + ground[k][j]:
                    ground[i][j] = ground[i][k] + ground[k][j]

    # for i in range(n):
    #     print(ground[i])
    answer = 0
    for i in range(n):
        tmp = []
        for j in range(n):
            if ground[i][j] <= m:
                tmp.append(j)

        res = 0
        for idx in tmp:
            res += items[idx]

        answer = max(answer, res)


    print(answer)