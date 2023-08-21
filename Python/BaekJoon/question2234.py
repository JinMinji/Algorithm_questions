# 20210519 성곽
from _collections import deque
n, m = map(int, input().split(' '))

walls = list()
for i in range(m):
    walls.append(list(map(int, input().split(' '))))

to_visit = deque()
visited = list()

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# 비트마스킹 어케해요

# 결과값 담을 변수 3개
room_num = 0
max_width = 0
max_width_by_del_wall = 0

# 방번호, 방넓이 담을 리스트
room_id = [[0 for i in range(n)] for j in range(m)]
room_width = [0]    # 방번호는 1부터시작이므로 앞에 0 넣어줌

# 모든 값을 확인
for i in range(m):
    for j in range(n):
        if [i, j] not in visited:   # 방문하지 않은 노드면, 그 노드부터 탐색시작
            to_visit.append([i, j])  # 방문할 노드에 넣어준다.
            room_num += 1           # 이어지는 모든 노드들 = 방 하나, 한번만 더해준다.
            width = 0               # 방의 넓이 (지역변수)
            while len(to_visit) > 0:    # 방문할 리스트에 아무것도 없을 때까지
                row, col = to_visit.popleft()
                visited.append([row, col])
                room_id[row][col] = room_num    # 방번호 적어주기
                for k in range(4):
                    tmp_x = row + dx[k]
                    tmp_y = col + dy[k]
                    if (walls[row][col] & (1 << k)) == 0 and [tmp_x, tmp_y] not in visited:
                        to_visit.append([tmp_x, tmp_y])   # 이어진 노드 찾아서 방문할 리스트에 넣어주기
                width += 1
            room_width.append(width)
            max_width = max(max_width, width)

for i in range(m):
    for j in range(n):
        for k in range(4):
            tmp_i = i + dx[k]
            tmp_j = j + dy[k]
            if (walls[i][j] & (1 << k)) != 0 and 0 <= tmp_i < m and 0 <= tmp_j < n :
                if room_id[tmp_i][tmp_j] != room_id[i][j]:
                    max_width_by_del_wall = max(max_width_by_del_wall,
                                            room_width[room_id[tmp_i][tmp_j]] + room_width[room_id[i][j]])

print(room_num)
print(max_width)
print(max_width_by_del_wall)

