# 2239 스도쿠, 골드4
import sys
import copy


def can(cur_board, cur, val):
    # 1. 가로 확인 -> board[i]
    # 2. 세로 확인 -> vertical[i]
    # 3. 사각형 확인 -> sqaure[i]

    i, j = cur
    # print("cur :", i, j)
    # 가로 확인
    if val in cur_board[i]:
        # print(val, "가로")
        return False
    # 세로 확인
    if vertical[j][val]:
        # print(val, "세로")
        return False

    # 3*3 정사각형 9개 확인
    i //= 3
    j //= 3
    if square[3*i+j][val]:
        # print(val, 3*i+j, "네모")
        return False

    return True


def find(board, idx):
    # for i in range(9):
    #     print(board[i])
    global result, blank_list, flag

    if flag:
        return

    if idx >= len(blank_list):
        # print("success")
        # print(board)
        result = copy.deepcopy(board)  #현재 담긴 내용을 결과 배열에 넣어준다.
        flag = True
        return

    else:
        # 다음으로 채울 빈칸을 뽑고,
        i, j = blank_list[idx]
        for n in range(1, 10):  # 1~9를 순서대로 넣어서 탐색해본다.
            if can(board, [i, j], n):   # 그 위치에 가능할 경우,
                board[i][j] = n         # 넣고,
                vertical[j][n] = 1
                square[(i // 3) * 3 + (j // 3)][n] = 1
                find(board, idx+1)      # 넣어서 돌리고
                board[i][j] = 0         # 보드는 다시 원래대로 돌려놓는다.
                vertical[j][n] = 0
                square[(i // 3) * 3 + (j // 3)][n] = 0
        # 다 돌았는데 넣을 게 없으면, 그냥 리턴.
    return


if __name__ == "__main__":
    sudoku = list()     # 기본 스도쿠 배열
    blank_list = list()     # 비어있는 위치 담아놓기
    vertical = [[0 for i in range(10)] for i in range(9)]
    square = [[0 for i in range(10)] for i in range(9)]
    for i in range(9):
        sudoku.append(list(map(int, sys.stdin.readline().rstrip('\n'))))
        for j in range(9):
            if sudoku[i][j] == 0:
                blank_list.append([i, j])
            else:
                vertical[j][sudoku[i][j]] = 1
                square[(i//3)*3 + (j//3)][sudoku[i][j]] = 1

    result = [] #결과를 담을 배열
    flag = False

    find(sudoku, 0)
    for i in range(9):
        print("".join(map(str, result[i])))

    # 0인 위치에 1~9중 가능한 숫자를 넣어본다.
    # 그 다음 0 위치에서도 동일하게 시도. 혹시 하나도 넣을 값이 없으면 back
