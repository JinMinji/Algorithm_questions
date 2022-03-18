def make_swirl(clockwise, cur, tmp_map):
    x, y = cur
    step = 0
    if clockwise:
        if x == 0 and y == 0:
            step = 1
        elif x == 0 and y != 0:
            step = 2
        elif x != 0 and y != 0:
            step = 3
        elif x != 0 and y == 0:
            step = 4

    else:
        if x == 0 and y == 0:
            step = 1
        elif x == 0 and y != 0:
            step = 4
        elif x != 0 and y != 0:
            step = 3
        elif x != 0 and y == 0:
            step = 2

    cur_val = 1

    if len(tmp_map) % 2 == 0:
        curve = len(tmp_map) // 2
    else:
        curve = len(tmp_map) // 2 + 1

    print(curve)

    # tmp_map[x][y] = cur_val
    for k in range(1, curve + 1):
        print(k)
        # →
        if (clockwise and step % 4 == 1) or (not clockwise and step % 4 == 2):
            for j in range(len(tmp_map) - k - 1):  # →
                print(x, y)
                cur_val += 1
                y += 1
                tmp_map[x][y] = cur_val
        # ↓
        elif (clockwise and step % 4 == 2) or (not clockwise and step % 4 == 1):
            for i in range(len(tmp_map) - k - 1):  # ↓
                print(x, y)
                cur_val += 1
                x += 1
                tmp_map[x][y] = cur_val
        # ←
        elif (clockwise and step % 4 == 3) or (not clockwise and step % 4 == 0):
            for j in range(len(tmp_map) - k - 1):  # →
                print(x, y)
                cur_val += 1
                y += -1
                tmp_map[x][y] = cur_val
        # ↑
        else:
            for i in range(len(tmp_map) - k - 1):  # ↓
                print(x, y, len(tmp_map) - k - 1)
                cur_val += 1
                x += -1
                tmp_map[x][y] = cur_val

        step += 1

        for _ in range(len(tmp_map)):
            print(tmp_map[_])

    return tmp_map


def solution(n, clockwise):
    answer = [[0 for i in range(n)] for i in range(n)]

    answer = make_swirl(clockwise, [0, 0], answer)
    answer = make_swirl(clockwise, [0, n - 1], answer)
    answer = make_swirl(clockwise, [n - 1, 0], answer)
    answer = make_swirl(clockwise, [n - 1, n - 1], answer)

    return answer


if __name__ == '__main__':
    print(solution(9, False))