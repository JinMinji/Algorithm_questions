# 소용돌이 예쁘게 출력하기

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, input().split(' '))

    # 0, 0 의 위치 찾기.
    # 주어진 행과 열을 기준으로 자르기 위해서 최소로 필요한 정사각형의 크기 구하기
    cur_i = max(abs(r1), abs(r2), abs(c1), abs(c2))
    cur_j = cur_i
    # print(cur_i, cur_j)

    width = max(cur_i, cur_j) * 2 + 1

    paper = [[0 for _ in range(width)] for _ in range(width)]

    cur_val = 1
    paper[cur_i][cur_j] = cur_val
    cur_val += 1

    inc = 0
    end = 0

    while inc <= len(paper)-1:
        inc += 1
        # print("inc : ", inc, "cur_val : ", cur_val)
        # 반시계방향
        # →
        for j in range(inc):
            cur_j += 1
            # print('→', cur_i, cur_j)
            if cur_j >= len(paper):
                end = 1
                break
            paper[cur_i][cur_j] = cur_val
            cur_val += 1

        if end:
            break
        # ↑
        for i in range(inc):
            cur_i -= 1
            # print('↑', cur_i, cur_j)
            if cur_i < 0:
                end = 1
                break
            paper[cur_i][cur_j] = cur_val
            cur_val += 1

        inc += 1
        # print("inc : ", inc, "cur_val : ", cur_val)

        if end:
            break
        # ←
        for j in range(inc):
            cur_j -= 1
            # print('←', cur_i, cur_j)
            if cur_j < 0:
                end = 1
                break
            paper[cur_i][cur_j] = cur_val
            cur_val += 1

        if end:
            break
        # ↓
        for i in range(inc):
            cur_i += 1
            # print('↓', cur_i, cur_j)
            if cur_i >= len(paper):
                end = 1
                break
            paper[cur_i][cur_j] = cur_val
            cur_val += 1

        if end:
            break

    max_len = len(str(cur_val))

    for i in range(width//2 + r1, width//2 + r2 + 1):
        for j in range(width//2 + c1, width//2 + c2 + 1):
            print(str(paper[i][j]).rjust(max_len), end=' ')
        print()


