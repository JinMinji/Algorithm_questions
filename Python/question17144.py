# 미세먼지 안녕!

dx = [0 , 0, -1, 1]
dy = [-1, 1, 0 , 0]


def spead_dust(dust_map, R, C):     # 미세먼지 확산
    result_map = [[0 for j in range(C)] for i in range(R)]

    for i in range(R):
        for j in range(C):
            if dust_map[i][j] == 0 or dust_map[i][j] == -1:
                continue
            else:
                add_val = dust_map[i][j]//5
                cnt = 0
                for _ in range(4):
                    x = i + dx[_]
                    y = j + dy[_]
                    if 0 <= x < R and 0 <= y < C and dust_map[x][y] != -1:
                        cnt += 1
                        result_map[x][y] += add_val
                result_map[i][j] += dust_map[i][j] - (add_val*cnt)

    return result_map


def run_air_cleaner(dust_map, R, C, cleaner_loc):     # 공기청정기 작동
    c_clockwise, clockwise = cleaner_loc[0], cleaner_loc[1]
    dust_map[c_clockwise][0] = -1
    dust_map[clockwise][0] = -1

    # 위쪽 공기청정기 반시계방향
    cur_val = 0
    for j in range(1, C):   # →
        dust_map[c_clockwise][j], cur_val = cur_val, dust_map[c_clockwise][j] #swap

    for i in range(c_clockwise -1, -1, -1):  # ↑
        dust_map[i][C-1], cur_val = cur_val, dust_map[i][C-1]

    for j in range(C-2, -1, -1):    # ←
        dust_map[0][j], cur_val = cur_val, dust_map[0][j]

    for i in range(1, c_clockwise):     # ↓
        dust_map[i][0], cur_val = cur_val, dust_map[i][0]

    # 아래쪽 공기청정기 시계방향
    cur_val = 0
    for j in range(1, C):       # →
        dust_map[clockwise][j], cur_val = cur_val, dust_map[clockwise][j]  # swap

    for i in range(clockwise+1, R):     # ↓
        dust_map[i][C-1], cur_val = cur_val, dust_map[i][C-1]

    for j in range(C - 2, -1, -1):      # ←
        dust_map[R-1][j], cur_val = cur_val, dust_map[R-1][j]

    for i in range(R-2, clockwise, -1):     # ↑
        dust_map[i][0], cur_val = cur_val, dust_map[i][0]

    return dust_map


if __name__ == '__main__':
    R, C, T = map(int, input().split(' '))

    dust_map = list()

    air_cleaner = list()

    for i in range(R):
        dust_map.append(list(map(int, input().split(' '))))
        if -1 in dust_map[i]:
            air_cleaner.append(i)

    for t in range(T):
        dust_map = spead_dust(dust_map, R, C)

        # print(t+1, "확산")
        # for i in range(len(dust_map)):
        #     print(dust_map[i])
        # print()

        dust_map = run_air_cleaner(dust_map, R, C, air_cleaner)

        # print(t + 1, "청정")
        # for i in range(len(dust_map)):
        #     print(dust_map[i])
        # print()

    result = 0
    for i in range(len(dust_map)):
        result += sum(dust_map[i])
        # print(dust_map[i])

    print(result + 2)       # 공기청정기 위치가 -1이니까