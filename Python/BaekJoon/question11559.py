# Puyo Puyo 골드4

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_puyo(c_map, i, j, col):   # 연결된 뿌요 찾아서 터트리기 - bfs
    global route

    need_visit = list()
    need_visit.append([i, j])
    route = list()
    route.append([i, j])

    while need_visit:
        cur_x, cur_y = need_visit.pop(0)

        for _ in range(4):
            x = cur_x + dx[_]
            y = cur_y + dy[_]
            if 0 <= x < 12 and 0 <= y < 6:
                if visited[x][y] == 0 and c_map[x][y] == col:
                    need_visit.append([x, y])
                    visited[x][y] = 1
                    route.append([x, y])


def puyo_fall(cur_map):     # 터진 후, 뿌요 바닥으로 내리기
    for j in range(6):
        char_l = list()
        for i in range(11, -1, -1):     # 밑에서부터 체크해서, 빈공간에 채워 넣기
            if cur_map[i][j] != '.':
                char_l.append(cur_map[i][j])
                cur_map[i][j] = '.'

        for _ in range(len(char_l)):
            cur_map[11-_][j] = char_l[_]

    return cur_map


if __name__ == '__main__':
    puyo_map = list()
    for i in range(12):
        puyo_map.append(list(input()))

    result = 0

    while True: # 더 터트릴 것이 있으면 계속확인.
        flag = False
        visited = [[0 for i in range(6)] for i in range(12)]  # 방문
        for i in range(12):
            for j in range(6):
                if puyo_map[i][j] != '.' and visited[i][j] == 0:  # 방문한 적 없으면,
                    visited[i][j] = 1
                    route = []
                    find_puyo(puyo_map, i, j, puyo_map[i][j])
                    if len(route) >= 4:
                        flag = True
                        for _ in range(len(route)):
                            tmp_x, tmp_y = route[_]
                            puyo_map[tmp_x][tmp_y] = '.'

        if not flag:
            break
        result += 1
        puyo_map = puyo_fall(puyo_map)
        # for p in range(len(puyo_map)):
        #     print(puyo_map[p])
        # print()

    print(result)
