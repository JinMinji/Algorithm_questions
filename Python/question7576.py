# 토마토 BFS

# M, N = map(int, input().split(" "))
#
# tomato_box = list()
#
# for _ in range(N):
#     box_row = list(map(int, input().split(" ")))
#     tomato_box.append(box_row)

# 입력받기 종료


M, N = 5, 5
tomato_box = [[1,0,0,0,0]
            ,[0,0,0,0,0]
            ,[0,0,0,0,0]
            ,[0,0,0,0,0]
            ,[0,0,0,0,1]]

ripe_tomato = list()
def dfs_tomato():
    tmp = ripe_tomato.pop(0)
    x, y = tmp[0], tmp[1]

    if x - 1 >= 0:
        if([x - 1, y] not in ripe_tomato):
            ripe_tomato.append([x - 1, y])
    if x + 1 < N:
        if ([x + 1, y] not in ripe_tomato):
            ripe_tomato.append([x + 1, y])
    if y - 1 >= 0:
        if ([x, y - 1]not in ripe_tomato):
            ripe_tomato.append([x, y - 1])
    if y + 1 < M:
        if ([x, y + 1] not in ripe_tomato):
            ripe_tomato.append([x, y + 1])

while( any(0 in l for l in tomato_box) ):
    for i in range(N):
        for j in range(M):
            if tomato_box[i][j] >= 1:
                if i-1 >= 0:
                    tomato_box[i-1][j] = 1
                if i+1 < N:
                    tomato_box[i+1][j] = 1
                if j-1 >= 0:
                    tomato_box[i][j-1] = 1
                if j+1 < M:
                    tomato_box[i][j+1] = 1
    result += 1

print(result)

