#20210609 욕심쟁이 판다
import sys

sys.setrecursionlimit(10000)
#이거를 써줘야만 통과됨

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_possible(x, y):
    return 0 <= x < n and 0 <= y < n


def long_live_panda(i, j, visited_dp):
    global answer
    if visited_dp[i][j] != -1:
        return visited_dp[i][j]

    tmp = 0
    visited_dp[i][j] = 1
    for _ in range(4):
        x = i + dx[_]
        y = i + dy[_]
        if is_possible(x, y):
            if bamboo_map[x][y] > bamboo_map[i][j]:
                tmp = max(tmp, long_live_panda(x, y, visited_dp))

    visited_dp[i][j] += tmp

    if answer < visited_dp[i][j]:
        answer = visited_dp[i][j]

    return visited_dp[i][j]


if __name__ == '__main__':
    n = int(input())

    bamboo_map = list()
    for i in range(n):
        bamboo_map.append(list(map(int, input().split())))

    visited_dp = [[-1 for _ in range(n)] for _ in range(n)]

    global answer
    answer = 0
    for i in range(n):
        for j in range(n):
            long_live_panda(i, j, visited_dp)

    print(answer)
