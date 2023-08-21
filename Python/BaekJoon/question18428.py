# 감시 피하기

import itertools

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상, 하, 좌, 우


def checking(pos, x, y):
    for i in range(len(pos)):
        if pos[i][0] in x:
            x.remove(pos[i][0])

        if pos[i][1] in y:
            y.remove(pos[i][1])

    if len(x) == 0 and len(y) == 0:
        return 1

    else:
        return 0


if __name__ == '__main__':
    N = int(input())

    info = list()

    for i in range(N):
        info.append(list(input().split(" ")))

    tea_x = list()
    tea_y = list()
    stu_x = list()
    stu_y = list()

    res_YN = 1

    for i in range(N):
        for j in range(N):
            if info[i][j] == 'T':   # 선생님 이면,
                for _ in range(4):  # 사이에 장애물이 들어올 새도 없이 학생과 붙어있으면, NO임
                    x = i + dx[_]
                    y = j + dy[_]
                    if 0 <= x < N and 0 <= y < N:
                        if info[x][y] == 'S':
                            res_YN = 0
                            break

                if i not in tea_x:
                    tea_x.append(i)

                if j not in tea_y:
                    tea_y.append(j)

            if info[i][j] == 'S':  # 학생이면,
                if i not in stu_x:
                    stu_x.append(i)

                if j not in stu_y:
                    stu_y.append(j)

        if not res_YN:  # 불가능 하면, 탐색 중지
            break

    danger_x = list()
    danger_y = list()

    for _ in range(len(tea_x)):
        if tea_x[_] in stu_x:
            danger_x.append(tea_x[_])

    for _ in range(len(tea_y)):
        if tea_y[_] in stu_y:
            danger_y.append(tea_y[_])

    if len(danger_x) > 3 or len(danger_y) > 3:  # 막아야하는 방향이 3개를 넘으면 방법이 없음
        res_YN = 0

    possible_pos = list()   # 방해물을 놓을 위치. 후보

    for i in range(len(danger_x)):
        for j in range(N):
            if info[danger_x[i]][j] == 'X':
                possible_pos.append([danger_x[i], j])

    for i in range(N):
        for j in range(len(danger_y)):
            if info[i][danger_y[j]] == 'X':
                possible_pos.append([i, danger_y[j]])

    # 후보 리스트에서 3개를 임의로 뽑은 후, 다 막을 수 있는지 확인한다.
    if len(possible_pos) <= 3:
        if checking(possible_pos, danger_x, danger_y):
            res_YN = 1

        else:
            res_YN = 0

    else:
        res_YN = 0
        tmp_com = list(itertools.combinations(possible_pos, 3))
        for k in range(len(tmp_com)):
            tmp_pos = list(tmp_com[k])

            if checking(tmp_pos, danger_x, danger_y):
                res_YN = 1
                break

    if res_YN:
        print('YES')
    else:
        print('NO')