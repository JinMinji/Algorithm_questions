# abc? 격자


dx = [0, 0, -1, 1]  #상하좌우로 탐색
dy = [-1, 1, 0, 0]
answer = 0


def find(cur, i, visited, check, cnt, grid):
    global answer

    if cnt[i] >= check[i]:     # 현재 카운트가
        i += 1
        for _ in range(i+1, 3):
            if to_visit[_]:
                x, y = to_visit[_]
                visited[x][y] = 1
                cnt[_] += 1
                find([x, y], _, visited, check, cnt, grid)
                i = _
                break

        if i >= 3 and all(0 not in v for v in visited): # a, b, c 다 찾았고, 방문하지않은 곳이 없을 때.
            answer += 1
            print(visited)
        answer += 1
        return

    cur_alpha = chr(i + 97)
    tmp_i, tmp_j = cur

    for _ in range(4):
        x = tmp_i + dx[_]
        y = tmp_j + dy[_]

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0:
            if grid[x][y] == cur_alpha:
                visited[x][y] = 1
                cnt[i] += 1
                find([x, y], i, visited, check, cnt, grid)

            elif grid[x][y] == '?':
                # 해당 알파벳 넣기
                visited[x][y] = 1
                # cnt[i] += 1      # cnt는 추가 안함. ? 위치이므로.
                find([x, y], i, visited, check, cnt, grid)
                visited[x][y] = 0


def solution(grid):
    global answer, to_visit
    to_visit = [[] for i in range(3)]
    visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]

    check = [0, 0, 0]

    for i in range(len(grid)):   # grid 돌면서
        for j in range(len(grid[0])):
            if grid[i][j] != '?':
                if check[ord(grid[i][j])-97] == 0:
                    to_visit[ord(grid[i][j])-97] = [i, j]

                check[ord(grid[i][j]) - 97] += 1

    cnt = [0 for i in range(3)]

    answer = 0
    for i in range(3):
        if to_visit[i]:
            x, y = to_visit[i]
            visited[x][y] = 1
            cnt[i] += 1
            find([x, y], i, visited, check, cnt, grid)
            break

    return answer


if __name__ == '__main__':
    print(solution(["??b", "abc", "cc?"]))
    print(solution(["aa?"]))