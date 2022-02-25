dp = list()


def dp_max(x, y, board):
    global dp

    if dp[x][y] == 'INF':   #구해 놓은 값이 없으면,
        if x-1 >= 0 and y-1 >= 0:
            if board[x][y] == 0:
                tmp_1 = max(dp_max(x - 1, y, board), -dp_max(x - 1, y, board))
                tmp_2 = max(dp_max(x, y - 1, board), -dp_max(x, y - 1, board))
                dp[x][y] = max(tmp_1, tmp_2)

            else:
                dp[x][y] = max(dp_max(x-1, y, board) + board[x][y], dp_max(x, y-1, board) + board[x][y])

        elif x-1 >= 0:
            if board[x][y] == 0:
                dp[x][y] = max(dp_max(x - 1, y, board), -dp_max(x - 1, y, board))

            else:
                dp[x][y] = dp_max(x - 1, y, board) + board[x][y]

        elif y-1 >= 0:
            if board[x][y] == 0:
                dp[x][y] = max(dp_max(x, y-1, board), -dp_max(x, y-1, board))

            else:
                dp[x][y] = dp_max(x, y-1, board) + board[x][y]

        else:
            dp[x][y] = board[x][y]

    return dp[x][y]


def solution(board):
    global dp
    dp = [['INF' for i in range(len(board))] for i in range(len(board))]
    answer = dp_max(len(board)-1, len(board)-1, board)

    return answer


if __name__ == '__main__':
    print(solution([[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]]	))
    print(solution([[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]]))