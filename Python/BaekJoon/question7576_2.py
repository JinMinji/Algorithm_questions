from collections import deque

# 토마토 BFS

M, N = map(int, input().split(" "))

tomato_box = list()

for _ in range(N):
    box_row = list(map(int, input().split(" ")))
    tomato_box.append(box_row)

# 입력받기 종료

ripe_tomatoes = deque()      # need_to_visit

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            ripe_tomatoes.append([i,j])

i_list = [1, -1, 0, 0]
j_list = [0, 0, 1, -1]

while len(ripe_tomatoes) > 0:
    i, j = ripe_tomatoes.popleft()

    for _ in range(4):
        tmpi = i + i_list[_]
        tmpj = j + j_list[_]

        if 0 <= tmpi < N and 0 <= tmpj < M and tomato_box[tmpi][tmpj] == 0:
            ripe_tomatoes.append([tmpi, tmpj])
            tomato_box[tmpi][tmpj] = tomato_box[i][j] + 1

chk = True
result = 0
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            chk = False
        result = max(result, tomato_box[i][j])

if chk:
    print(result-1)
else:
    print(-1)


