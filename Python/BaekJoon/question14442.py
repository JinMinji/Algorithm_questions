# 20210519 벽 부수고 이동하기 2

from collections import deque

def chk(x, y, w):
    return 0 <= x < N and 0 <= y < M and not visited[x][y][w]

def bfs(start):
    q = deque([start])
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while q:
        cur_x, cur_y, wall = q.popleft()
        dist = visited[cur_x][cur_y][wall] + 1

        if [cur_x, cur_y] == [N - 1, M - 1]:
            return visited[cur_x][cur_y][wall]

        for _ in range(4):
            next_x, next_y = cur_x + dx[_], cur_y + dy[_]
            if chk(next_x, next_y, wall):
                if not graph[next_x][next_y]:
                    visited[next_x][next_y][wall] = dist
                    q.append((next_x, next_y, wall))
                elif wall < K:
                    visited[next_x][next_y][wall + 1] = dist
                    q.append((next_x, next_y, wall + 1))

    return -1


if __name__ == '__main__':
    N, M, K = map(int, input().split(' '))
    graph = list()
    for n in range(N):
        graph.append(list(input()))

    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    # 3차원 배열
    visited[0][0] = [1] * (K + 1)

    print(bfs((0, 0, 0)))