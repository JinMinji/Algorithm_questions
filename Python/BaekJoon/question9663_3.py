# N-Queen
import sys
import copy
sys.setrecursionlimit(10 ** 6)


def dfs(queens):
    global result

    print(queens)
    if len(queens) == N:
        result += 1
        return

    r = len(queens) - 1  # row

    for j in range(len(queens)):    # col
        y = queens[j]
        if j == y:
            # 세로 줄 겹침
            return
        gap = r - j
        if j + gap == r and (y + gap == j or y - gap == j): # 아래쪽 대각선만 확인
            return

        else:
            tmp_queens = copy.deepcopy(queens)
            dfs(tmp_queens.append(i))
            print(tmp_queens)


if __name__ == '__main__':
    N = int(input())    # 칸, 퀸 개수

    result = 0

    for i in range(N):
        queens = list()
        queens.append(i)
        dfs(queens)

    print(result)
