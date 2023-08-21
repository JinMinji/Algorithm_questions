# 감시 피하기

import itertools
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상, 하, 좌, 우


def checking(pos, info, teachers):
    tmp_info = copy.deepcopy(info)
    for _ in range(3):
        tmp_i, tmp_j = pos[_]
        tmp_info[tmp_i][tmp_j] = 'O'

    for t in range(len(teachers)):
        i, j = teachers[t]
        for _ in range(4):
            for plus in range(1, len(info)):
                x = i + (dx[_] * plus)
                y = j + (dy[_] * plus)
                if 0 <= x < len(info) and 0 <= y < len(info):
                    if tmp_info[x][y] == 'S':
                        return 0
                    if tmp_info[x][y] == 'O':
                        break

    return 1


if __name__ == '__main__':
    N = int(input())

    info = list()

    for i in range(N):
        info.append(list(input().split(" ")))

    possible_pos = list()

    teachers = list()

    for i in range(N):
        for j in range(N):
            if info[i][j] == 'X':   # 장애물을 둘 수 있는 빈 공간이면, 후보
                possible_pos.append([i, j])

            elif info[i][j] == 'T':   # 선생님 위치 체크   # 선생님은 최대 5명임
                teachers.append([i, j])

    tmp_com = list(itertools.combinations(possible_pos, 3))

    res_YN = 0

    for _ in range(len(tmp_com)):
        if checking(list(tmp_com[_]), info, teachers):
            res_YN = 1
            break

    if res_YN:
        print('YES')
    else:
        print('NO')