#뱀, 골드 5
dx = [0, 1, 0, -1]  # → ↓ ← ↑
dy = [1, 0, -1, 0]


def go_snake():
    global time
    time += 1
    # print("현재 뱀 위치 : ", snake)
    #
    # print("지도 ↓")
    # for i in range(N):
    #     print(board[i])
    # print()

    x, y = snake[-1]    # snake 리스트 맨 뒤에 뱀의 head위치가 담겨있음.
    x += dx[direction]  # 방향대로 x, y이동
    y += dy[direction]

    if 0 <= x < N and 0 <= y < N:   # 범위 밖이면 -> 벽에 부딪힘. -> 종료
        if board[x][y] == 0:    # 비어있는 공간.
            board[x][y] = 1     # 뱀머리로 채워주고
            snake.append([x, y])    # 머리가 이동한 위치 붙여서 뱀위치 갱신
            tail_x, tail_y = snake.pop(0)   # 사과 안먹었으니까, 꼬리도 함께 이동. 꼬리위치 pop()해주기
            board[tail_x][tail_y] = 0   # 꼬리위치 다시 비어있는 공간으로 만들어주기

        elif board[x][y] == 2:  # 사과가 있는 공간.
            board[x][y] = 1     # 뱀머리로 채워주고
            snake.append([x, y])    # 머리가 이동한 위치 붙여서 뱀위치 갱신
            # 사과를 먹었으므로, 꼬리는 이동하지 않는다.

        else:  # board[x][y] == 1: 몸통 만남
            # 몸통을 만나면 게임 종료.
            return True

    else:  # 벽만남
        # 벽을 만나면 게임 종료
        return True

    return False


if __name__ == '__main__':
    N = int(input())
    K = int(input())

    board = [[0 for i in range(N)] for i in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        board[x-1][y-1] = 2     # 사과는 2

    L = int(input())

    snake = [[0, 0]]
    board[0][0] = 1

    time = 0
    direction = 0
    finish = False

    for l in range(L):
        X, C = map(str, input().split())
        X = int(X)
        for t in range(time, X):
            finish = go_snake()
            if finish:
                break

        if finish:
            break

        if C == 'L':    # 왼쪽으로 회전
            direction = (direction - 1) % 4
        else:   # C == "D"  # 오른쪽으로 회전
            direction = (direction + 1) % 4

    while not finish:
        finish = go_snake()

    print(time)

