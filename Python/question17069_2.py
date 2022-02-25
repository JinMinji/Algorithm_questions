#20210727 파이프 옮기기 2 두번째 풀이

graph = list()

# 파이프 방향별로 담아줄 3차원 리스트
dp_direction = list()

dx = [0, 1, 1]
dy = [1, 0, 1]


def is_possible(x, y):
    if x < len(graph) and y < len(graph) and graph[x][y] != 1:
        return True

    else:
        return False


def dp_pipe():
    # 0:가로, 1:세로, 2:대각선
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == -1:
                continue

            for _ in range(3):
                tmp_i = i + dx[_]
                tmp_j = j + dy[_]
                if is_possible(tmp_i, tmp_j):
                    if _ == 0:      #가로
                        dp_direction[_][tmp_i][tmp_j] += dp_direction[0][i][j] + dp_direction[2][i][j]
                    elif _ == 1:    #세로
                        dp_direction[_][tmp_i][tmp_j] += dp_direction[1][i][j] + dp_direction[2][i][j]
                    else:           #대각선 가로에서 올때 + 세로에서 올때, 대각선으로 올때
                        if is_possible(i, j+1) and is_possible(i+1, j):
                            dp_direction[_][tmp_i][tmp_j] += dp_direction[0][i][j] + dp_direction[1][i][j] + dp_direction[2][i][j]


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        graph.append(list(map(int, input().split())))

    dp_direction = [[[0 for i in range(N)] for i in range(N)] for i in range(3)]
    dp_direction[0][0][1] = 1   #처음에 놓인 위치
    dp_pipe()

    total = 0
    for _ in range(3):
        total += dp_direction[_][N-1][N-1]

    print(total)
