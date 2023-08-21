# 20210519 성곽
from _collections import deque

def bfs(i, j):
    to_visit = deque()
    to_visit.append([i,j])
    width = 0  # 방의 넓이
    while to_visit:    # 방문할 리스트에 아무것도 없을 때까지
        row, col = to_visit.popleft()
        room_id[row][col] = room_num    # 방번호 적어주기
        width += 1
        for k in range(4):
            x = row + dx[k]
            y = col + dy[k]
            if (walls[row][col] & (1 << k)) == 0 and visited[x][y] == 0:
                to_visit.append([x, y])   # 이어진 노드 찾아서 방문할 리스트에 넣어주기
                visited[x][y] = 1
    room_width.append(width)

def bfs_max(i,j):
    visited[i][j] = 1
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if (walls[i][j] & (1 << k)) != 0 and 0 <= x < m and 0 <= y < n:
            if room_id[x][y] != room_id[i][j]:
                return room_width[room_id[x][y]] + room_width[room_id[i][j]]
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split(' '))

    walls = list()
    for i in range(m):
        walls.append(list(map(int, input().split(' '))))

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    # 비트마스킹 어케해요

    # 결과값 담을 변수 3개
    room_num = 0
    max_width = 0
    max_width_by_del_wall = 0

    # 방번호, 방넓이 담을 리스트
    room_id = [[0 for i in range(n)] for j in range(m)]
    room_width = [0]  # 방번호는 1부터시작이므로 앞에 0 넣어줌

    visited = [[0 for i in range(n)] for j in range(m)]
    # 모든 값을 확인
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:  # 방문하지 않은 노드면, 그 노드부터 탐색시작
                room_num += 1  # 이어지는 모든 노드들 = 방 하나, 한번만 더해준다.
                visited[i][j] = 1
                bfs(i, j)

    visited = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                max_width_by_del_wall = max(max_width_by_del_wall, bfs_max(i, j))

    print(room_num)
    max_width = max(room_width)
    print(max_width)
    print(max_width_by_del_wall)

