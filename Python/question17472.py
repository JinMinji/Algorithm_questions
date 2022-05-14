# 다리 만들기2
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 섬 넘버링해주는 함수
def island_check(num, i, j):
    global island_map
    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if 0 <= x < len(island_map) and 0 <= y < len(island_map[0]):
            if island_map[x][y] == 1:
                island_map[x][y] = num
                island_check(num, x, y)


#다른 섬을 만날때까지 직선 탐색하는 함수, 다리의 길이를 return
def find_other(island_num, cur, direction, cnt):
    global island_map
    i = cur[0]
    j = cur[1]

    x = i + dx[direction]
    y = j + dx[direction]
    if 0 <= x < len(island_map) and 0 <= y < len(island_map[0]):
        if island_map[x][y] == 0:
            return find_other(island_num, [x, y], direction, cnt+1)
        elif island_map[x][y] == island_num:
            return [0, 0]
        else:   # 다른 섬을 만나면
            if cnt == 2:
                return [0, 0]
            else:
                #다른 섬 번호와, 다리길이를 함께 return
                return [island_map[x][y], cnt]


#현 위치에서 다른 섬에 뻗을 수 있는 다리의 최단 길이 찾기
def make_road(cur, visited):
    global island_map, min_bridges
    i = cur[0]
    j = cur[1]
    cur_num = island_map[i][j]
    for _ in range(4):  # 좌, 우, 상, 하 네 방향 탐색
        x = i + dx[_]
        y = j + dy[_]
        # 바다면, 그 쪽으로 쭉 뻗어본다.
        if 0 <= x < len(island_map) and 0 <= y < len(island_map[0]):
            if island_map[x][y] == 0:
                # 이 방향으로 쭈욱 뻗어가보기!
                tmp = find_other(cur_num, [x, y], _, 1)
                if tmp[0] != 0:
                    min_bridges[-(cur_num)-1][-(tmp[0]) - 1] = min(min_bridges[-(cur_num)-1][-(tmp[0]) - 1], tmp[1])
            if island_map[x][y] != 0 and [x,y] not in visited:   #바다가 아니면,
                # 바다가 나올 때까지 탐색 해야되는데! 여기서 방문체크를 해줘야하는디
                visited.append([x, y])
                make_road([x, y], visited)


# 다리는 꺾일 수 없고
# 다리는 2칸 이상이어야하며
# 가로모양 다리는 섬과 가로로 만나야하고,
# 세로모양 다리는 섬과 세로로 만나야한다
# 모든 섬이 연결되어 있어야 한다

# 모든섬이 연결되어 있으려면, 섬이 최소 하나의 다리를 갖되,
# 최소 조건을 만족할 것이므로, 나와 이미 연결된 섬으로 중복되는 다리를 만들지는 않는다.
# N개의 섬이 있을 때 각 섬에서 다리를 설치하는 경우의 수는 N-1개
# N-1은 1~5개
# 5개의 섬에 놓을 수 있는 다리의 길이를 다 체크해서
# 다리는 겹쳐도되니까 다른 다리 고려하지 않고, 최단인 다리를 선택,
# 다음 섬으로 넘어가서 동일하게 반복. 다리를 넘어가는 순서는 그냥 숫자로 넘버링.

if __name__ == "__main__":
    N, M = map(int, input().split())

    island_map = list()

    for i in range(N):
        island_map.append(list(map(int, sys.stdin.readline().split())))

    cur = -1
    start_list = list()
    for i in range(N):
        for j in range(M):
            if island_map[i][j] == 1:
                start_list.append([i, j])
                island_check(cur, i, j)
                cur -= 1

    # for i in range(N):
    #     print(island_map[i])
    # print(start_list)
    min_bridges = [[N*M for i in range(len(start_list))] for i in range(len(start_list))]
    min_bridges[0][0] = 0  #나에게로 오는 비용은 0
    result = 0
    make_road(start_list[0], [])