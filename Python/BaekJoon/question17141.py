# 17141, 연구소2, 골드4
import sys
from itertools import combinations
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solutions(loc_list, tmp):
    global result, lab
    visited = copy.deepcopy(tmp)

    # print(loc_list, result)
    # for i in range(len(visited)):
    #     print(*visited[i])
    # print()

    to_visit = copy.deepcopy(loc_list)
    while to_visit:
        i, j = to_visit.pop(0)
        time = visited[i][j]
        for _ in range(4):
            x = i + dx[_]
            y = j + dy[_]
            if 0 <= x < len(visited) and 0 <= y < len(visited[0]):
                if lab[x][y] != 1 and (visited[x][y] == -1 or visited[x][y] > time+1):
                    visited[x][y] = time+1
                    to_visit.append([x, y])
                elif lab[x][y] == 2 and [x, y] not in loc_list:
                    visited[x][y] = time + 1
                    to_visit.append([x, y])

    if all(-1 not in visited[x] for x in range(len(visited))):
        tmp_max = max(map(max, visited))
        result = min(result, tmp_max)
    #
    # for i in range(len(visited)):
    #     print(*visited[i])
    #
    # print()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    lab = list()
    virus_loc = list()
    visited = [[-1 for i in range(N)] for i in range(N)]
    for i in range(N):
        lab.append(list(map(int, sys.stdin.readline().split())))
        for j in range(N):
            if lab[i][j] == 2:
                virus_loc.append([i, j])

            if lab[i][j] != 0:
                visited[i][j] = 0

    result = N*N
    # M은 10개 이하, 2도 10개 이하.. 다 돌아도 된다.

    tmp = list(map(list, combinations(virus_loc, M)))
    while tmp:
        # print("what")
        cur = tmp.pop()
        solutions(cur, visited)

    print(result)