# 무기 공학, 골드 5
import sys
sys.setrecursionlimit(10000)


def boomerang(x, y, cur_total):
    global res_max

    if y == M:
        x += 1
        y = 0

    if x == N:
        res_max = max(res_max, cur_total)
        return

    if visited[x][y] == 0:
        # ㄱ
        if 0 <= x+1 < N and 0 <= y-1 < M:
            if visited[x+1][y] == 0 and visited[x][y-1] == 0:
                visited[x + 1][y] = 1
                visited[x][y-1] = 1
                visited[x][y] = 1
                boomerang(x, y+1, cur_total + 2*wood_map[x][y] + wood_map[x+1][y] + wood_map[x][y-1])
                visited[x + 1][y] = 0
                visited[x][y - 1] = 0
                visited[x][y] = 0

        # ┛
        if 0 <= x-1 < N and 0 <= y-1 < M:
            if visited[x-1][y] == 0 and visited[x][y-1] == 0:
                visited[x - 1][y] = 1
                visited[x][y-1] = 1
                visited[x][y] = 1
                boomerang(x, y+1, cur_total + 2*wood_map[x][y] + wood_map[x-1][y] + wood_map[x][y-1])
                visited[x - 1][y] = 0
                visited[x][y - 1] = 0
                visited[x][y] = 0

        # ㄴ
        if 0 <= x-1 < N and 0 <= y+1 < M:
            if visited[x-1][y] == 0 and visited[x][y+1] == 0:
                visited[x - 1][y] = 1
                visited[x][y + 1] = 1
                visited[x][y] = 1
                boomerang(x, y+1, cur_total + 2*wood_map[x][y] + wood_map[x-1][y] + wood_map[x][y+1])
                visited[x - 1][y] = 0
                visited[x][y + 1] = 0
                visited[x][y] = 0

        # ┎
        if 0 <= x+1 < N and 0 <= y+1 < M:
            if visited[x+1][y] == 0 and visited[x][y+1] == 0:
                visited[x + 1][y] = 1
                visited[x][y + 1] = 1
                visited[x][y] = 1
                boomerang(x, y+1, cur_total + 2*wood_map[x][y] + wood_map[x+1][y] + wood_map[x][y+1])
                visited[x + 1][y] = 0
                visited[x][y + 1] = 0
                visited[x][y] = 0

    boomerang(x, y + 1, cur_total)


if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    wood_map = list()
    for i in range(N):
        wood_map.append(list(map(int, input().split(' '))))

    visited = [[0 for i in range(M)] for i in range(N)]
    res_max = 0

    boomerang(0, 0, 0)
    print(res_max)

