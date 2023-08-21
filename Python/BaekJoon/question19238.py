# 19238, 스타트 택시, 골드3
import sys

dx = [1, 0, 0, -1]  # 하, 우, 좌, 상
dy = [0, 1, -1, 0]


def find_shortest(loc):
    min_dist = INF
    min_idx = -1
    for key, values in guests.items():
        if values[0] == 0 and min_dist > graph[loc][key]:
            min_idx = key
            min_dist = graph[loc][key]

    if min_idx != -1:
        # 방문 체크
        guests[min_idx][0] = 1

    return min_idx


def taxi(cur_loc):
    global F
    # print(cur_loc, F)
    next_guest = find_shortest(cur_loc)
    # print(next_guest)
    if next_guest == -1:
        # print("here")
        # 모든 승객들 방문 완료거나 어떤 승객도 방문할 수 없음.
        for v in guests.values():
            if v[0] == 0:
                F = -1
        return
    if F >= graph[cur_loc][next_guest]:
        # print(F, cur_loc, next_guest, guests[next_guest][1])
        # print(graph[cur_loc][next_guest])
        # print(graph[next_guest][guests[next_guest][1]])
        # 승객까지 갈 수 있으면 가고,
        F -= graph[cur_loc][next_guest]
        if F >= graph[next_guest][guests[next_guest][1]]:  # 도착지까지 갈 수 있으면.
            F += graph[next_guest][guests[next_guest][1]]
            taxi(guests[next_guest][1])
        else:  # 갈수 없으면? 종료
            # print("here")
            F = -1
            return
    else:  # 승객까지 못가면? 종료.
        F = -1
        return


if __name__ == "__main__":
    N, M, F = map(int, sys.stdin.readline().split())

    taxi_map = list()
    for i in range(N):
        taxi_map.append(list(map(int, sys.stdin.readline().split())))

    baekjoon_x, baekjoon_y = map(int, sys.stdin.readline().split())

    guests = dict()

    for i in range(M):
        sx, sy, ex, ey = map(int, sys.stdin.readline().split())
        guests[N * (sx - 1) + sy - 1] = [0, N * (ex - 1) + ey - 1]

    # print(guests.items())

    INF = float('inf')
    graph = [[INF for i in range(N * N)] for i in range(N * N)]
    for i in range(N):
        for j in range(N):
            if taxi_map[i][j] != 1:
                for _ in range(2):  # 하, 우 두 방향만 보면 됨. 어차피 위에서부터 내려오니까 좌, 상은 이미 제크됨
                    x = i + dx[_]
                    y = j + dy[_]
                    if 0 <= x < N and 0 <= y < N and taxi_map[x][y] == 0:
                        graph[N * i + j][N * x + y] = 1
                        graph[N * x + y][N * i + j] = 1

    for _ in range(N * N):
        graph[_][_] = 0
    for k in range(N * N):
        for i in range(N * N):
            for j in range(N * N):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # for i in range(N * N):
    #     print(*graph[i])

    # 현재 위치에서 부터 운행 시작
    taxi(N * (baekjoon_x - 1) + baekjoon_y - 1)

    print(F)