def make_basic_route(x, y, H, W):
    global basic_route

    if basic_route[x][y] != 0:
        return basic_route[x][y]

    else:
        if 0 <= y - 1:
            basic_route[x][y] += make_basic_route(x, y - 1, H, W)
            # print(make_basic_route(x, y - 1, H, W))
        if H >= x + 1:
            basic_route[x][y] += make_basic_route(x + 1, y, H, W)
            # print(make_basic_route(x + 1, y, H, W))

        # 대각선은 딱 한번만 갈 수 있으니, 따로 체크
        # if x+1 < H and y+1 < W and [x+1, y+1] in diagonals:
        #     route[x][y] += make_route(x+1, y+1)

        basic_route[x][y] = basic_route[x][y] % 10000019

        return basic_route[x][y]


def make_tmp_route(x, y, route):
    if route[x][y] != 0:
        return route[x][y]

    else:
        if 0 <= y - 1:
            route[x][y] += make_tmp_route(x, y - 1, route)
            # print(make_basic_route(x, y - 1, route))
        if len(route) > x + 1:
            route[x][y] += make_tmp_route(x + 1, y, route)
            # print(make_basic_route(x + 1, y, route))

        route[x][y] = route[x][y] % 10000019

        return route[x][y]


def solution(width, height, diagonals):
    answer = 0
    global basic_route

    diagonals.sort(key=lambda x: x[1])
    # 대각선이 없다면 무조건 오른쪽, 위로 향하는 경로만 존재. 왼쪽으로 되돌아 올 수 없음.
    # 대각선이 있다면 한칸 왼쪽으로 돌아오는 것이 가능.

    # map[0][1]으로 오는 경로는
    # map[0][0]으로 오는 경로 + map[1][0]으로 오는 경로

    # route[x][y] => map[x][y]으로 오는 경로의 수 % 10,000,019
    basic_route = [[0 for i in range(width + 1)] for i in range(height + 1)]

    basic_route[height][0] = 1

    make_basic_route(0, width, height, width)
    # for i in range(len(basic_route)):
    #     print(basic_route[i])

    for i in range(len(diagonals)):
        # 특정 대각선을 지나는 경로
        dx, dy = diagonals[i]
        dy = width - dy + 1
        print(dx, dy)
        # 대각선이 2,2에 있다면,
        # basic_route[1][1] = basic_route[1][0] + basic_route[2][1] + basic_route[2][2]
        # 이후 새로 route 리스트를 만들고, [1][1]에서부터 찾아 올라간다.
        start_val = basic_route[dx-1][dy-1] + basic_route[dx][dy]
        print(start_val, )
        tmp_route = [[0 for i in range(width-dy+2)] for i in range(dx)]

        tmp_route[dx-1][0] = start_val
        # for _ in range(len(tmp_route)):
        #     print(tmp_route[_])

        answer += make_tmp_route(0, width-dy+1, tmp_route)
        print('cur_answer', make_tmp_route(0, width-dy+1, tmp_route))

    return answer


if __name__ == '__main__':
    # print(solution(2, 2, [[1, 1], [2, 2]]))
    print(solution(51, 37, [[17, 19]]))