def make_route(x, y, H, W):
    global route

    if route[x][y] != 0:
        return route[x][y]

    else:
        if 0 <= y - 1:
            route[x][y] += make_route(x, y - 1, H, W, route)
            print(make_route(x, y - 1, H, W, route))
        if H >= x + 1:
            route[x][y] += make_route(x + 1, y, H, W, route)
            print(make_route(x + 1, y))

        # 대각선은 딱 한번만 갈 수 있으니, 따로 체크
        # if x+1 < H and y+1 < W and [x+1, y+1] in diagonals:
        #     route[x][y] += make_route(x+1, y+1)

        route[x][y] = route[x][y] % 10000019

        return route[x][y]


def solution(width, height, diagonals):
    answer = 0
    global route

    diagonals.sort(key=lambda x: x[1])
    # 대각선이 없다면 무조건 오른쪽, 위로 향하는 경로만 존재. 왼쪽으로 되돌아 올 수 없음.
    # 대각선이 있다면 한칸 왼쪽으로 돌아오는 것이 가능.

    # map[0][1]으로 오는 경로는
    # map[0][0]으로 오는 경로 + map[1][0]으로 오는 경로

    # route[x][y] => map[x][y]으로 오는 경로의 수 % 10,000,019
    route = [[0 for i in range(width+1)] for i in range(height+1)]

    route[height][0] = 1
    for i in range(len(diagonals)):
        # 특정 대각선을 꼭 지나는 경로
        dx, dy = diagonals[i]
        tmp = make_route(dx-1, dy-1, dx, dy, route) + make_route(dx-1, dy-1, dx, dy, route)
        tmp_route = [[0 for i in range(height-dx+1)] for i in range(width-dy+1)]
        tmp_route[0][width-dy] = tmp
        answer += make_route(0, width-dy, dx, dy, route)


    answer = make_route(0, width, height, width, route) + len(diagonals)*(width+1)
    # print(make_route(2, 1))
    print(route)

    return answer


if __name__ == '__main__':
    print(solution(2, 2, [[1,1],[2,2]]))