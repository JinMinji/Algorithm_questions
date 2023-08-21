from collections import deque


def isRange(x, y):
    return 0 <= x < N and 0 <= y < N


def solve():
    q = deque()
    q.append((0, 0, int(board[0][0]), '+'))
    global res_max, res_min

    while q:
        x, y, num, op = q.popleft()

        if x == N-1 and y == N-1:
            res_max = max(res_max, num)
            res_min = min(res_min, num)
            continue

        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]

            if not isRange(nx, ny):
                continue

            tmp = num
            if '0' <= board[nx][ny] <= '5':
                if op == '+':
                    tmp = num + int(board[nx][ny])
                elif op == '-':
                    tmp = num - int(board[nx][ny])
                else:
                    tmp = num * int(board[nx][ny])
            else:
                op = board[nx][ny]

            q.append((nx, ny, tmp, op))


if __name__ == '__main__':
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        board[i] = list(map(str, input().split()))

    res_max, res_min = int(-1e9), int(1e9)

    dx = [1, 0]
    dy = [0, 1]

    solve()

    print(res_max, res_min)