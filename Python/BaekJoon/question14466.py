#소가 길을 건너간 이유 6, 골드 4
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def cnt_cant_go(cow):
    global K, farm, bridges, result
    x, y = cow

    start = x*N + y
    cnt = 0

    to_visit = list()
    visited = [0 for i in range(N*N)]
    visited[start] = 1
    to_visit.append(start)

    while to_visit:
        cur = to_visit.pop(0)

        if farm[cur] == 1:
            cnt += 1

        i = cur // N
        j = cur % N
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if 0 <= x < N and 0 <= y < N:
                tmp = x*N + y
                if visited[tmp] == 1:
                    continue

                if tmp in bridges[cur]:
                    continue

                to_visit.append(tmp)
                visited[tmp] = 1

    result += K-cnt


if __name__ == '__main__':
    N, K, R = map(int, input().split())

    #그냥 1차원으로 생각한다..
    farm = [0 for i in range(N*N)]
    bridges = [[] for i in range(N*N)]

    # for i in range(N):
    #     for j in range(N):
    #         for _ in range(4):
    #             x = i+dx[_]
    #             y = j+dy[_]
    #             if 0 <= x < N and 0 <= y < N:
    #                 bridges[i*N+j].append(x*N+y)

    for r in range(R):
        r1, c1, r2, c2 = map(int, input().split())
        bridges[(r1-1)*N+c1-1].append((r2-1)*N+c2-1)
        bridges[(r2-1)*N+c2-1].append((r1-1)*N+c1-1)

    cows = list()
    for k in range(K):
        x, y = map(int, input().split())
        cows.append([x-1, y-1])
        farm[(x-1)*N+(y-1)] = 1

    result = 0
    for k in range(K):
        cnt_cant_go(cows[k])

    print(result//2)