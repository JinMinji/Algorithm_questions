# 20210527 소문난 칠공주
import itertools

# S : 이다솜파
# Y : 임도연파
# S가 4명 이상

dx = [0,0,1,-1] # 좌, 우, 상, 하
dy = [-1,1,0,0]

def isPossible(x,y):
    return 0<=x<5 and 0<=y<5

def isConnected(graph):
    start = graph[0]
    to_visit = list()
    to_visit.append(start)
    visited = [start]

    while to_visit:
        i, j = to_visit.pop(0)
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if isPossible(x,y) and [x,y] in graph and [x,y] not in visited:
                to_visit.append([x,y])
                visited.append([x,y])

    if len(visited) == 7:
        return True
    else:
        return False


if __name__ == '__main__':
    class_map = list()
    for i in range(5):
        class_map.append(input())
# 입력 : class_map
    index_map = [[0,0],[0,1],[0,2],[0,3],[0,4]
                 ,[1,0],[1,1],[1,2],[1,3],[1,4]
                 ,[2,0],[2,1],[2,2],[2,3],[2,4]
                 ,[3,0],[3,1],[3,2],[3,3],[3,4]
                 ,[4,0],[4,1],[4,2],[4,3],[4,4]]

    all_com = list(itertools.combinations(index_map, 7))
    check_list = list()

    for com in all_com:
        S_Cnt = 0
        for k in com:
            x, y = k
            if class_map[x][y] == 'S':
                S_Cnt +=1

        if S_Cnt >= 4:
            check_list.append(com)

    result = 0

    for check in check_list:
        if isConnected(check):
            result += 1

    print(result)