dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_lake(cur, num):
    global row, column, maps, visited, lakes
    i, j = cur

    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if 0 <= x < row and 0 <= y < column:
            if maps[x][y] == 0 and visited[x][y] == 0:  #물이면서, 방문하지 않았을 때
                visited[x][y] = num
                if x == 0 or y == 0 or x == row-1 or y == column-1:  # 바다면,
                    lakes[num-1] = [-1] # 호수배열 초기화
                    break
                else:
                    lakes[num-1].append([x, y])
                    find_lake([x, y], num)
            elif maps[x][y] == 0 and visited[x][y] != num:  #물인데 다른 호수 번호가 적혀있다?
                lakes[num - 1] = [-1]      # 이전 호수 탐색할 때, 바다라서 탐색을 멈췄다는 뜻이므로 호수배열 초기화


def solution(rows, columns, lands):
    global row, column, maps, visited, lakes
    row = rows
    column = columns

    maps = [[0 for i in range(columns)] for i in range(rows)]

    for i in range(len(lands)):
        x, y = lands[i]
        maps[x-1][y-1] = 1

    answer = [rows*columns, -1]

    visited = [[0 for i in range(columns)] for i in range(rows)]
    lakes = list()
    lake_num = 1
    for i in range(1, rows-1):    #벽에 닿아있으면 바다니까..
        for j in range(1, columns-1):
            if maps[i][j] == 0 and visited[i][j] == 0:
                lakes.append([])
                lakes[lake_num-1].append([i, j])
                visited[i][j] = lake_num
                find_lake([i, j], lake_num)
                lake_num += 1

            if maps[i][j] == 1:
                visited[i][j] = -1

    # print(lakes)
    for lake in lakes:
        if lake[0] != -1:
            answer[0] = min(answer[0], len(lake))
            answer[1] = max(answer[0], len(lake))

    if answer[0] == rows*columns:
        answer = [-1, -1]
    return answer


if __name__ == "__main__":
    print(solution(9, 7, [[2, 2], [2, 3], [2, 5], [3, 2], [3, 4], [3, 5], [3, 6], [4, 3], [4, 6], [5, 2], [5, 5], [6, 2], [6, 3], [6, 4], [6, 6], [7, 2], [7, 6], [8, 3], [8, 4], [8, 5]]))
    print(solution(5, 6, [[2, 2], [2, 3], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]))
    print(solution(5, 7, [[2, 5], [3, 3], [3, 4], [3, 5], [4, 3]]))