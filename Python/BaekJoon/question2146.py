# 20210519 다리만들기
from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isPossible(x, y, graph):    # 범위를 벗어나지않고, 바다일 때
    return 0 <= x < N and 0 <= y < N and graph[x][y] == 0

def isPossible2(x, y):          # 범위만 체크
    return 0 <= x < N and 0 <= y < N


beaches = deque()       # 해변가 - 바다와 맞닿은 땅의 좌표를 담아줄 deque

def bfs_naming(start, island_name):     # 섬에 이름붙여주는 BFS. 섬을 구분해야하므로.
    to_visit = deque()
    to_visit.append(start)

    while to_visit:
        i, j = to_visit.popleft()

        for index in range(4):
            x = i + dx[index]
            y = j + dy[index]
            if isPossible(x, y, island_map):
                if country[x][y] == 1:      # 땅이면
                    island_map[x][y] = island_name  # 이름넣어주기
                    to_visit.append([x, y])
                else:   # 바다가 맞닿아 있으면,
                    if [i,j] not in beaches:        # 바닷가는 미리 넣어주기.
                        beaches.append([i,j])       # 땅 칸임


def bfs():      # 섬에서 또 다른 섬으로 가는 최단 경로 찾기.
    min_dist = N*N      # 일단 최대값을 넣어줌.

    while beaches:      # 바닷가큐에 남은 값이 없을 때까지
        to_visit = deque()  # 큐에서 하나씩 꺼내서 확인
        to_visit.append(beaches[0])     # bfs에 쓸 to_visit에 넣어준다. (start)
        tmpi, tmpj = beaches.popleft()
        name = island_map[tmpi][tmpj]   # 시작 위치의 섬 번호를 저장.
        tmp_map = copy.deepcopy(island_map)

        while to_visit:
            i, j = to_visit.popleft()

            for index in range(4):  # 상, 하, 좌, 우 탐색
                x = i + dx[index]
                y = j + dy[index]
                if isPossible2(x, y):   # 범위 안에 있는 값일 때
                    if tmp_map[x][y] > 0:        # 땅을 만나면: 거리 확인
                        if tmp_map[x][y] != name:    # 만난 땅이 내 땅의 번호랑 다를 때 (다른 섬일 때)
                            min_dist = min(min_dist, abs(tmp_map[i][j])) # 땅으로 오기 이전, 바다에서의 거리값과 비교.
                    elif tmp_map[x][y] == 0:     # 방문하지 않은 바다를 만나면: 계속 탐색
                        if tmpi == i and tmpj == j: # 땅부터 시작하니까     # 땅일때는 island[i][j] 값을 0으로 두고, -1 해줘야함.
                            tmp_map[x][y] = - 1
                        else:
                            tmp_map[x][y] = tmp_map[i][j] - 1

                        if min_dist <= abs(tmp_map[x][y]):  # 섬이 1이라서, 음수로 체크. 이미 min_dist값 이상인 경로는 탐색 패스.
                            continue
                        to_visit.append([x,y])

                    #else: #이미 방문한 바다를 만나면. 패스
    return(min_dist)

if __name__ == '__main__':
    N = int(input())
    country = list()
    for i in range(N):
        country.append(list(map(int, input().split(" "))))

    island_map = [[0 for n in range(N)] for m in range(N)]
    island_name = 0
    for i in range(N):
        for j in range(N):
            if island_map[i][j] == 0 and country[i][j] == 1:
                island_name += 1
                island_map[i][j] = island_name
                bfs_naming([i,j], island_name)


    print(bfs())