#14503, 로봇청소기, 골드 5
import sys
import copy

dx = [-1, 0, 1, 0]  # ↑ → ↓ ←
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    r, c, d = map(int, sys.stdin.readline().split())

    cleaning_map = []
    for i in range(N):
        cleaning_map.append(list(map(int, sys.stdin.readline().split())))

    test_print = copy.deepcopy(cleaning_map)
    visited = [[0 for j in range(M)] for i in range(N)]

    cur = [r, c]
    visited[r][c] = 1
    cur_cnt = 0     # 4방향을 다 봤는지 확인.
    result = 1
    test_print[r][c] = 'X'
    while True:
        i, j = cur
        d = (d - 1) % 4
        x = i + dx[d]
        y = j + dy[d]
        cur_cnt += 1
        # print("cur :", result, ",", i, j)
        if 0 <= x < N and 0 <= y < M and cleaning_map[x][y] == 0:   #범위 내, 벽이 아닐 경우
            if visited[x][y] == 0:  # 청소하지 않은 곳일 때
                visited[x][y] = 1
                cur = [x, y]
                cur_cnt = 0
                result += 1
                test_print[x][y] = result

            else:   # 청소한 곳일 때
                # print(x, y, "청소완료")
                if cur_cnt == 4:    #이미 4방향을 돌았을 경우? 후진한다.
                    # print("4방향 탐색 완료, 후진", d)
                    x = i - dx[d]
                    y = j - dy[d]
                    # print("후진", x, y)
                    if 0 <= x < N and 0 <= y < M and cleaning_map[x][y] == 0:
                        cur = [x, y]
                        cur_cnt = 0
                    else:
                        break
        else:
            # print(x, y, "벽")
            if cur_cnt == 4:  # 이미 4방향을 돌았을 경우? 후진한다.
                # print("4방향 탐색 완료, 후진", d)
                x = i - dx[d]
                y = j - dy[d]
                # print("후진", x, y)
                if 0 <= x < N and 0 <= y < M and cleaning_map[x][y] == 0:
                    cur = [x, y]
                    cur_cnt = 0
                else:
                    break

    # for i in range(N):
    #     for j in range(M):
    #         print(str(test_print[i][j]).zfill(2), end=" ")
    #     print()
    # print()
    print(result)


