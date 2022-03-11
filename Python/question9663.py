#N-Queen
result = 0


def can_attack(chess_board, cur_loc):
    global result

    x, y = cur_loc
    if x == len(chess_board)-1:     # 마지막줄까지 가면 +1
        result += 1
        return

    for i in range(len(chess_board)):   #공격 가능한 위치 표시
        chess_board[x][i] = 1   # 세로
        chess_board[i][y] = 1   # 가로
        if 0 <= x - i and 0 <= y - i:   # ↖
            chess_board[x - i][y - i] = 1
        if 0 <= x - i and y + i < len(chess_board):   # ↗
            chess_board[x - i][y + i] = 1
        if x + i < len(chess_board) and 0 <= y - i:     # ↙
            chess_board[x + i][y - i] = 1
        if x + i < len(chess_board) and y + i < len(chess_board):   # ↘
            chess_board[x+i][y+i] = 1

    # for i in range(len(chess_board)):
    #     print(chess_board[i])

    for j in range(len(chess_board)):   # 다음 줄, 퀸을 높을 수 있는 위치에서 또 탐색.
        if chess_board[x+1][j] == 0:
            print('next, ', x+1, j)
            can_attack(chess_board, [x+1, j])


if __name__ == '__main__':
    N = int(input())

    for j in range(N):      #row 기준으로 첫번째 줄 부터 선택.
        c_board = [[0 for i in range(N)] for i in range(N)]
        print('start', 0, j)
        can_attack(c_board, [0, j])

    print(result)
