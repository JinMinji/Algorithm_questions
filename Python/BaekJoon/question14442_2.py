from collections import deque

# 20210519 벽 부수고 이동 2

def ispossible(x,y):        #범위 체크
    return 0 <= x < N and 0 <= y < M

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    to_visit = deque()
    to_visit.append(start)

    while to_visit:
        i, j, w = to_visit.popleft()

        if i == N - 1 and j == M - 1: # 종료 지점에 도착했으면 return
            return visited[i][j][w]

        for index in range(4):
            x = i + dx[index]
            y = j + dy[index]
            if ispossible(x, y):
                if graph[x][y] == '0':     # 값이 0이면 : 벽이 아니면서
                    if visited[x][y][w] == 0:   # 방문한 적이 없으면.
                        to_visit.append([x, y, w])
                        visited[x][y][w] = visited[i][j][w] + 1  # 방문한 값을 넣어주고,
                elif w < K:     # 벽이지만, 아직 벽을 더 부술 수 있다면
                    if visited[x][y][w+1] == 0:       # 그리고 이미 부순 벽이 아니라면!
                        visited[x][y][w + 1] = visited[i][j][w] + 1
                        to_visit.append([x, y, w + 1])

    return -1       # 종료지점에 도착하지 못함

if __name__ == '__main__':
    N, M, K = map(int, input().split(' '))
    graph = list()
    for n in range(N):
        graph.append(list(input()))

    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    # 3차원 배열
    visited[0][0] = [1] * (K + 1) # 시작 칸은 처음칸부터 세므로 1로 변경

    print(bfs([0, 0, 0]))   # 맨 처음 칸에서 시작, 부순 벽의 개수 0개