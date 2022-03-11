# N-Queen
result = 0
N = 0


def cnt_way(cnt, chess_board):
    global result

    if cnt >= N:  # 마지막줄까지 가면 +1
        result += 1
        return

    for j in range(N):  # 다음 줄, 퀸을 높을 수 있는 위치에서 또 탐색.
        if chess_board[cnt][j] == 0:
            cnt_way(cnt + 1, can_attack(chess_board, [cnt - 1, j]))


def can_attack(chess_board, cur_loc):   # 현 시점에서 공격 가능한 위치 체크
    x, y = cur_loc
    for i in range(len(chess_board)):  # 공격 가능한 위치 표시
        chess_board[x][i] = 1  # 세로
        chess_board[i][y] = 1  # 가로
        if 0 <= x - i and 0 <= y - i:  # ↖
            chess_board[x - i][y - i] = 1
        if 0 <= x - i and y + i < len(chess_board):  # ↗
            chess_board[x - i][y + i] = 1
        if x + i < len(chess_board) and 0 <= y - i:  # ↙
            chess_board[x + i][y - i] = 1
        if x + i < len(chess_board) and y + i < len(chess_board):  # ↘
            chess_board[x + i][y + i] = 1

    return chess_board


if __name__ == '__main__':
    N = int(input())

    cnt = 0

    for s in range(N):
        cnt += 1
        c_board = [[0 for j in range(N)] for i in range(N)]
        cnt_way(cnt + 1, can_attack(c_board, [0, s]))

    print(result)
