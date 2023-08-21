#20210521 녹색 옷 입은 애가 젤다지?

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def isPossible(x,y):
    return 0<=x<N and 0<=y<N

def cheap_route(start):
    to_visit = list()
    to_visit.append(start)
    while to_visit:
        i, j = to_visit.pop(0)
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if isPossible(x,y):
                if cheapest_map[x][y] > cheapest_map[i][j]+cave[x][y]:
                    cheapest_map[x][y] = cheapest_map[i][j]+cave[x][y]
                    to_visit.append([x,y])

if __name__ == '__main__':
    result_list = list()
    while True:
        N = int(input())
        cave = list()
        for i in range(N):
            cave.append(list(map(int, input().split(" "))))

        if N == 0:
            break

        cheapest_map = [[N*N*9 for i in range(N)] for j in range(N)]
        # visited = [[0 for i in range(N)] for j in range(N)]
        cheapest_map[0][0] = cave[0][0]
        cheap_route([0,0])
        result_list.append(cheapest_map[N-1][N-1])

    for i in range(len(result_list)):
        print("Problem %d: %d" %(i+1, result_list[i]))


