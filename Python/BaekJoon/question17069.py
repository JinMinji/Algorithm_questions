#20210727 파이프 옮기기 2

graph = list()
dp_way = list()

# 가로일 때 H
# 세로일 때 V
# 대각선일 때 D
# 파이프 방향별로도 담아줄 리스트를 만들어 둔다.
dp_direction = list()


def dp(direction, x, y):
    if graph[x][y] == 1:
        dp[direction][x][y] = 0
        return dp[direction][x][y]

    if x == 0 and y == 0:
        dp_direction[direction][x][y] = 0
        return dp_direction[direction][x][y]

    if direction == 0:  #가로
        if x == 0 and y == 1:   #초기값
            dp_direction[direction][x][y] = 1
            return dp_direction[direction][x][y]

        if y == 0 or graph[x][y-1] == 1:
            dp_direction[direction][x][y] = 0
            return dp_direction[direction][x][y]

        dp_direction[direction][x][y] = dp(0, x, y-1) + dp(2, x, y-1)
        return dp_direction[direction][x][y]

    elif direction == 1:    #세로
        if x == 0 or graph[x-1][y] == 1:
            dp_direction[direction][x][y] = 0
            return dp_direction[direction][x][y]

        dp_direction[direction][x][y] = dp(1, x-1, y) + dp(2, x-1, y)
        return dp_direction[direction][x][y]

    else:   #대각선
        if (x == 0 or y == 0) or graph[x-1][y] == 1 or graph[x][y-1] == 1 or graph[x-1][y-1] == 1:
            dp_direction[direction][x][y] = 0
            return dp_direction[direction][x][y]

        dp_direction[direction][x][y] = dp(0, x-1, y-1) + dp(1, x-1, y-1) + dp(2, x-1, y-1)
        return dp_direction[direction][x][y]


def ways(x, y):
    if graph[x][y] == 1:    #벽이면
        dp_way[x][y] = 0
        return dp_way[x][y]

    if dp_way[x][y] != -1:  #이미 구했으면
        return dp_way[x][y]

    # dp_way 구하기
    # 현 위치에서의 경우의 수는,
    # 왼쪽에서 가로로 오는 경우, 위쪽에서 세로로 오는 경우, 왼쪽위에서 대각선으로 오는 경우!
    dp_way[x][y] = dp(0, x, y) + dp(1, x, y) + dp(2, x, y)

    dp_way[x][y] = ways(x-1, y-1)

    return dp_way[x][y]


if __name__ == '__main__':
    N = int(input())
    pipe_map = list()
    for i in range(N):
        pipe_map.append(list(map(int, input().split())))

    dp_way = [[-1 for i in range(N)] for i in range(N)]
    dp_direction = [[[-1 for i in range(N)] for i in range(N)] for i in range(3)]
    graph = pipe_map
    print(ways(len(graph)-1, len(graph)-1))
