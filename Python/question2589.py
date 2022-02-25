# 20210824 보물상자

if __name__ == '__main__':
    N, M = map(int, input().split())

    treasure_map = list()

    for i in range(N):
        treasure_map.append(input())

    dist_map = [[-1 for i in range(M*N)] for j in range(M*N)]

    dx = [0, 1]
    dy = [1, 0]

    for i in range(N):
        for j in range(M):
            for _ in range(2):
                x = i + dx[_]
                y = j + dy[_]
                if x < N and y < M and treasure_map[x][y] == 'L':
                    dist_map[i * M + j][x * M + y] = 1
                    dist_map[x * M + y][i * M + j] = 1

    for i in range(N*M):
        for j in range(N*M):
            for k in range(N*M):
                if dist_map[i][k] == -1 or dist_map[k][j] == -1:
                    continue

                if dist_map[i][k] != -1 and dist_map[k][j] != -1:
                    if dist_map[i][j] == -1:
                        dist_map[i][j] = dist_map[i][k] + dist_map[k][j]
                    elif dist_map[i][j] > dist_map[i][k] + dist_map[k][j]:
                        dist_map[i][j] = dist_map[i][k] + dist_map[k][j]

    print(max(map(max, dist_map)))



