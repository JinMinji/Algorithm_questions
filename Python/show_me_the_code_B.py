# Drop 7
import sys

def run_game(board):
    visited = [[0 for i in range(7)] for i in range(7)]
    for i in range(7):
        for j in range(7):
            if board[i][j] != 0:
                x = i
                y = j
                for


def fall(board):
    for j in range(7):
        tmp_list = []
        for i in range(7):
            if board[i][j] != 0:
                tmp_list.append(board[i][j])

        tmp_list = [0 for i in range(7-len(tmp_list))] + tmp_list
        for i in range(7):
            board[i][j] = tmp_list[i]


if __name__ == "__main__":
    game_board = list()
    tops = []
    result = 0
    for i in range(7):
        game_board.append(list(map(int, sys.stdin.readline().split())))
        for j in range(7):
            if game_board[i][j] != 0:
                result += 1

    for j in range(7):
        for x in range(7):
            if game_board[x][j] != 0:
                tops.append(x-1)
                break

    ball = int(input())

    for j in range(7):
        game_board[tops[j]][j] = ball
        run_game(game_board)
        game_board[tops[j]][j] = 0

    #공을 놓을 수 있는 방법 -> 7가지

