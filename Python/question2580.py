#스도쿠, 골드4
import copy


def find_num(idx, answer_list):
    # print(idx)
    # print(answer_list)
    global ans
    if idx == len(empty_lst):
        ans = copy.deepcopy(answer_list)
        # print(ans)
        return

    x, y = empty_lst[idx]

    for i in range(1, 10):
        if is_ok(x, y, i):
            answer_list.append(i)
            find_num(idx+1, answer_list)
            answer_list.pop()


def is_ok(x, y, num):
    if num in sudoku[x]:
        return False
    for _ in range(9):
        if num == sudoku[_][y]:
            return False

    i_start = 0
    if x%3 == 0:
        i_start = x
    elif x%3 == 1:
        i_start = x-1
    else:
        i_start = x-2

    j_start = 0
    if y%3 == 0:
        j_start = y
    elif y%3 == 1:
        j_start = y-1
    else:
        j_start = y-2

    for i in range(3):
        for j in range(3):
            if num == sudoku[i_start+i][j_start+j]:
                return False

    return True


if __name__ == "__main__":
    sudoku = list()
    empty_lst = list()

    for i in range(9):
        cur_row = list(map(int, input().split()))
        sudoku.append(cur_row)

    ans = []
    find_num(0, [])
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j]


    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print()