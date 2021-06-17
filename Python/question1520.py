# 20210608 내리막길
import sys

sys.setrecursionlimit(10000)
#이거를 써줘야만 통과됨

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def is_possible(x, y, cur):
    if 0 <= x < M and 0 <= y < N:
        if downhill_map[cur[0]][cur[1]] < downhill_map[x][y]:
            return True
    return False


def find_easy_route(end, visited_list):
    i, j = end
    if visited_list[i][j] != -1:
        return visited_list[i][j]

    else:
        tmp = 0
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if is_possible(x, y, end):
                tmp += find_easy_route([x, y], visited_list)

        visited_list[i][j] = tmp
        return visited_list[i][j]

if __name__ == '__main__':
    M, N = map(int, input().split())
    visited_dp = [[-1 for i in range(N)] for j in range(M)]
    # 방문하지않은 곳은 -1

    downhill_map = list()
    for i in range(M):
        downhill_map.append(list(map(int, input().split())))

    visited_dp[0][0] = 1
    print(find_easy_route([M-1, N-1], visited_dp))
