#16724, 피리 부는 사나이, 골드3
import sys


def find(x, y, cur_cnt):
    global maps, visited, result

    if visited[x][y] != 0:
        if visited[x][y] == cur_cnt:
            # print(x, y)
            result += 1
            return

        else:
            return

    visited[x][y] = cur_cnt

    if maps[x][y] == 'U':
        if 0 <= x-1:
            find(x-1, y, cur_cnt)
        else:
            result += 1

    elif maps[x][y] == 'D':
        if x+1 < len(maps):
            find(x+1, y, cur_cnt)
        else:
            result += 1

    elif maps[x][y] == 'L':
        if 0 <= y-1:
            find(x, y-1, cur_cnt)
        else:
            result += 1

    else:   # 'R'
        if y + 1 < len(maps[0]):
            find(x, y+1, cur_cnt)
        else:
            result += 1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maps = list()
    for i in range(N):
        maps.append(list(sys.stdin.readline().rstrip("\n")))

    visited = [[0 for i in range(M)] for i in range(N)]
    cnt = 1

    result = 0
    # print(maps)
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                find(i, j, cnt)
                cnt += 1

    # print(visited, result)
    print(result)

