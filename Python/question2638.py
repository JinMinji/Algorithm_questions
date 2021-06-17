#20210605 치즈

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1] # 상하좌우

def isPossible(x,y):
    return 0<=x<N and 0<=y<M

def melting_time(cheese):
    time = 0

    while any(1 in l for l in cheese):
        to_visit = list()
        visited = [[0 for i in range(M)] for j in range(N)]
        to_visit.append([0, 0])  # 모서리에는 치즈가 없고, 내부에 있는 0은 외부공기로 안따지니까 그냥 0,0부터 연결된 애들 쭉 탐색
        # melting_cnt = [[0 for i in range(M)] for j in range(N)]
        visited[0][0] = 1

        while to_visit:
            i, j = to_visit.pop(0)
            for _ in range(4):
                x = i + dx[_]
                y = j + dy[_]
                if isPossible(x,y):
                    if cheese[x][y] >= 1:
                        cheese[x][y] += 1
                    elif visited[x][y] == 0:
                        to_visit.append([x,y])
                        visited[x][y] = 1

        for i in range(N):
            for j in range(M):
                if cheese[i][j] == 0:
                    continue
                elif cheese[i][j] >= 3:
                    cheese[i][j] = 0
                elif cheese[i][j] == 2:
                    cheese[i][j] = 1

        time += 1

    return time

if __name__ == "__main__":
    N, M = map(int, input().split(" "))

    cheese_map = list()
    for i in range(N):
        cheese_map.append(list(map(int, input().split(" "))))

    print(melting_time(cheese_map))