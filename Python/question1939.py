# BFS

country, bridge = map(int,input().split(' '))
bridges = dict()
#딕셔너리로 구현

# 경로가 있는지 찾는 BFS 함수
# 인자 C는 최대중량

def bfs(c):
    # start -> end경로가 있는지, 그 경로가 가진 최대무게가 c보다 큰지
    visited = [False]*(country+1)
    need_visit = list()
    need_visit.append(island1) #시작지점을, 탐색리스트에 넣고
    visited[island1] = True

    while need_visit:
        node = need_visit.pop(0)
        for y, weight in bridges[node].items():
            if not visited[y] and weight >= c: # 최대중량보다 큰지 확인해본다.
                visited[y] = True
                need_visit.append(y)

    return visited[island2]

# 다리에 대한 정보 입력받기
for i in range(bridge):
    lst = list(map(int, input().split(' ')))
    if lst[0] in bridges:
        bridges[lst[0]][lst[1]] = lst[2]

    else:
        bridges[lst[0]] = {lst[1]:lst[2]}

    if lst[1] in bridges:
        bridges[lst[1]][lst[0]] = lst[2]

    else:
        bridges[lst[1]] = {lst[0]:lst[2]}


# 두 섬 입력받기
island1, island2 = map(int,input().split(" "))

min_val = 1
max_val = 1000000000

# 이진 탐색으로 최대무게 찾기
result = min_val
while (min_val <= max_val):
    mid = (min_val+max_val)//2
    if bfs(mid): # 중간값 이상의 경로가 있는지,
        result = mid
        min_val = mid+1 # 있으면 중간값 위에서 찾는다
    else:
        max_val = mid-1 # 없으면 중간값 아래에서 찾는다

print(result)
