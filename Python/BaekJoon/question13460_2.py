# 구슬 탈출 2, 골드 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rolling(cnt, cur_R, cur_B):
    # 상 하 좌 우
    red_x, red_y = cur_R
    blue_x, blue_y = cur_B

    for _ in range(4):
        while True:
            tmp_red_x = red_x + dx[_]
            tmp_blue_y = blue_x + dy[_]


if __name__ == '__main__':
    N, M = map(int, input().split())

    board = list()
    R_pos = [-1, -1]
    B_pos = [-1, -1]
    for i in range(N):
        board.append(list(input()))
        if 'R' in board[i]:
            R_pos = [i, board[i].index('R')]
            board[i][board[i].index('R')] = '.'
        if 'B' in board[i]:
            R_pos = [i, board[i].index('B')]
            board[i][board[i].index('B')] = '.'

    result = -1

    rolling(0, R_pos, B_pos)

    print(result)
