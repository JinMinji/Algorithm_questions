# 낚시왕, 골드 2

def shark_move(d, s, r, c, R, C):
    if d == 1 or d == 2:
        if d == 1:
            r -= s
        elif d == 2:
            r += s
        while r <= 0 or r > R:
            if r <= 0:
                r = abs(r - 2)  # -2면, abs(-2-2) -> 4
                d = 2

            elif r > R:
                r = 2 * R - r  # R-(r-R)        # 5행이고 8이면, 5-(8-5) -> 2
                d = 1

    else:
        if d == 3:
            c += s
        else:
            # print('-->', c, s, c+s)
            c -= s
        while c <= 0 or c > C:
            if c <= 0:
                c = abs(c - 2)
                d = 3

            else:  # elif c > C:
                c = 2 * C - c      # cur_c = 8, C= 4 면,
                d = 4

    return d, r, c


if __name__ == '__main__':
    R, C, M = map(int, input().split())

    shark_map = [[-1 for i in range(C+1)] for i in range(R+1)]
    shark_list = list()

    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        shark_list.append([r, c, s, d, z])
        if shark_map[r][c] == -1:   # 해당 칸에 상어가 없을 때
            shark_map[r][c] = i

        else:                       # 해당 칸에 이미 상어가 있을 때
            if z > shark_list[shark_map[r][c]][4]:  # 크기가 같은 경우는 없음
                shark_list[shark_map[r][c]] = []     # 작은 상어쪽 정보는 지워버린다
                shark_map[r][c] = i
            else:
                shark_list[i] = []                      # 작은 상어쪽 정보는 지워버린다

# ------------------- 입력 받기 종료 --------------------

    result = 0
    for j in range(1, C+1):  # 낚시왕은 오른쪽으로만 이동, 총 C초간 낚시
        # step 1. 낚시왕 이동, 땅과 제일 가까운 상어 잡기
        print('낚시왕 위치', j)
        for i in range(1, R+1):
            if shark_map[i][j] != -1:
                tmp = shark_map[i][j]
                result += shark_list[tmp][4]
                print('잡힌 상어 :', chr(tmp+65), '현재 점수 :', result)
                shark_list[tmp] = []    # 잡힌 상어 정보 지우기
                shark_map[i][j] = -1    # 지도에서 상어 지우기
                # 제일 위에 한 마리 잡으면 다음 칸으로 이동!
                break

        # step 2. 상어 이동하기
        for i in range(len(shark_list)):
            if not shark_list[i]:   # 이미 잡히거나, 잡아먹힌 상어
                continue
            else:
                r, c, s, d, z = shark_list[i]
                shark_map[r][c] = -1    # 지도에서 이동 전 위치 지우기
                d, r, c = shark_move(d, s, r, c, R, C)

                shark_list[i] = [r, c, s, d, z]     # 변경된 위치, 방향으로 상어 정보 업데이트

                print('shark', chr(i+65), 'move to', r, c)

                if shark_map[r][c] == -1:  # 해당 칸에 상어가 없을 때
                    shark_map[r][c] = i

                else:  # 해당 칸에 이미 상어가 있을 때
                    if shark_map[r][c] < i:
                        print('collision in ', r, c, chr(i + 65), 'with', chr(shark_map[r][c] + 65))
                        if z > shark_list[shark_map[r][c]][4]:  # 크기가 같은 경우는 없음
                            shark_list[shark_map[r][c]] = []  # 작은 상어쪽 정보는 지워버린다
                            shark_map[r][c] = i
                        else:
                            shark_list[i] = []  # 작은 상어쪽 정보는 지워버린다

                    else:
                        shark_map[r][c] = i

    print('최종 점수 : ', end="")
    print(result)