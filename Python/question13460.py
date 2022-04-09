# 구슬 탈출 2, 골드 1

def rolling(cnt, curR, curB):
    global result
    if cnt >= 11 or result != -1:
        return

    Rx, Ry = curR
    Bx, By = curB

    # ↑, ↓
    if Ry == By:  # 같은 줄이면 구슬끼리의 위치도 고려해줘야함.
        if Rx < Bx:
            # 같은줄, 레드가 위쪽에 있을때 ↑
            canR, canB = True, True
            nextR, nextB = Rx, Bx
            for i in range(N - 2):
                tmpRx = Rx - i
                if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                    if board[tmpRx][Ry] == 'O':
                        # Blue도 같이 빠지면 무효.
                        for j in range(N - 3):
                            tmpBx = Bx - j
                            if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                                if board[tmpBx][By] == 'O':
                                    return
                        result = cnt
                        return
                    nextR = tmpRx
                else:
                    canR = False
            # 잠시 막아두기
            board[nextR][Ry] = '#'
            for i in range(N - 3):
                tmpBx = Bx - i
                if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                    if board[tmpBx][By] == 'O':
                        board[nextR][Ry] = '.'
                        return
                    nextB = tmpBx
                else:
                    canB = False

            board[nextR][Ry] = '.'
            rolling(cnt + 1, [nextR, Ry], [nextB, By])


            # 같은 줄, 레드가 위쪽에 있을 때 ↓
            canR, canB = True, True
            nextR, nextB = Rx, Bx
            for i in range(N - 3):
                tmpBx = Bx - i
                if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                    if board[tmpBx][By] == 'O':
                        return
                    nextB = tmpBx
                else:
                    canB = False

            # 잠시 막아두기
            board[nextB][By] = '#'
            for i in range(N - 2):
                tmpRx = Rx - i
                if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                    if board[tmpRx][Ry] == 'O':
                        result = cnt
                        board[nextB][By] = '.'
                        return
                    nextR = tmpRx
                else:
                    canR = False
            board[nextB][By] = '.'
            rolling(cnt + 1, [nextR, Ry], [nextB, By])


        else:
            # 같은줄, 레드가 아래쪽에 있을때 ↑
            canR, canB = True, True
            nextR, nextB = Rx, Bx
            for i in range(N - 3):
                tmpBx = Bx - i
                if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                    if board[tmpBx][By] == 'O':
                        return
                    nextB = tmpBx
                else:
                    canB = False

            # 잠시 막아두기
            board[nextB][By] = '#'
            for i in range(N - 2):
                tmpRx = Rx - i
                if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                    if board[tmpRx][Ry] == 'O':
                        result = cnt
                        board[nextB][By] = '.'
                        return
                    nextR = tmpRx
                else:
                    canR = False
            board[nextB][By] = '.'
            rolling(cnt + 1, [nextR, Ry], [nextB, By])

            # 같은줄, 레드가 아래쪽에 있을때 ↓
            canR, canB = True, True
            nextR, nextB = Rx, Bx
            for i in range(N - 2):
                tmpRx = Rx - i
                if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                    if board[tmpRx][Ry] == 'O':
                        # Blue도 같이 빠지면 무효.
                        for j in range(N - 3):
                            tmpBx = Bx - j
                            if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                                if board[tmpBx][By] == 'O':
                                    return
                        result = cnt
                        return
                    nextR = tmpRx
                else:
                    canR = False
            # 잠시 막아두기
            board[nextR][Ry] = '#'
            for i in range(N - 3):
                tmpBx = Bx - i
                if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                    if board[tmpBx][By] == 'O':
                        board[nextR][Ry] = '.'
                        return
                    nextB = tmpBx
                else:
                    canB = False

            board[nextR][Ry] = '.'
            rolling(cnt + 1, [nextR, Ry], [nextB, By])

    else:
        # ↑
        canR, canB = True, True
        nextR, nextB = Rx, Bx
        for i in range(N-2):
            tmpRx = Rx - i
            tmpBx = Bx - i
            if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                if board[tmpRx][Ry] == 'O':
                    result = cnt
                    return
                nextR = tmpRx
            else:
                canR = False

            if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                if board[tmpBx][By] == 'O':
                    return
                nextB = tmpBx
            else:
                canB = False

        rolling(cnt+1, [nextR, Ry], [nextB, By])

        # ↓
        canR, canB = True, True
        nextR, nextB = Rx, Bx
        for i in range(N-2):
            tmpRx = Rx + i
            tmpBx = Bx + i
            if canR and 0 < tmpRx < N - 1 and board[tmpRx][Ry] != '#':
                if board[tmpRx][Ry] == 'O':
                    result = cnt
                    return
                nextR = tmpRx
            else:
                canR = False

            if canB and 0 < tmpBx < N - 1 and board[tmpBx][By] != '#':
                if board[tmpBx][By] == 'O':
                    return
                nextB = tmpBx
            else:
                canB = False
        rolling(cnt + 1, [nextR, Ry], [nextB, By])

    # ←, →
    if Rx == Bx:  # 같은 줄이면 구슬끼리의 위치도 고려해줘야함.
        if Ry < By:
            # 같은줄, 레드가 왼쪽에 있을때 ←
            canR, canB = True, True
            nextR, nextB = Ry, By
            for i in range(M - 2):
                tmpRy = Ry - i
                if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                    if board[Rx][tmpRy] == 'O':
                        # Blue도 같이 빠지면 무효.
                        for j in range(M - 3):
                            tmpBy = By - i
                            if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                                if board[Bx][tmpBy] == 'O':
                                    return
                        result = cnt
                        return
                    nextR = tmpRy
                else:
                    canR = False
            # 잠시 막아두기
            board[Rx][nextR] = '#'

            for i in range(M - 3):
                tmpBy = By - i
                if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                    if board[Bx][tmpBy] == 'O':
                        board[Rx][nextR] = '.'
                        return
                    nextB = tmpBy
                else:
                    canB = False

            board[Rx][nextR] = '.'
            rolling(cnt + 1, [Rx, nextR], [Bx, nextB])

            # 같은 줄, 레드가 왼쪽에 있을 때 →
            canR, canB = True, True
            nextR, nextB = Ry, By
            for i in range(M - 3):
                tmpBy = By + i
                if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                    if board[Bx][tmpBy] == 'O':
                        return
                    nextB = tmpBy
                else:
                    canB = False

            # 잠시 막아두기
            board[Bx][nextB] = '#'
            for i in range(M - 2):
                tmpRy = Ry + i
                if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                    if board[Rx][tmpRy] == 'O':
                        result = cnt
                        board[Bx][nextB] = '.'
                        return
                    nextR = tmpRy
                else:
                    canR = False

            board[Bx][nextB] = '.'
            rolling(cnt + 1, [Rx, nextR], [Bx, nextB])


        else:
            # 같은줄, 레드가 오른쪽에 있을때 ←
            canR, canB = True, True
            nextR, nextB = Ry, By
            for i in range(M - 3):
                tmpBy = By - i
                if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                    if board[Bx][tmpBy] == 'O':
                        return
                    nextB = tmpBx
                else:
                    canB = False

            # 잠시 막아두기
            board[Bx][nextB] = '#'
            for i in range(M - 2):
                tmpRy = Ry - i
                if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                    if board[Rx][tmpRy] == 'O':
                        result = cnt
                        board[Bx][nextB] = '.'
                        return
                    nextR = tmpRy
                else:
                    canR = False
            board[Bx][nextB] = '.'
            rolling(cnt + 1, [Rx, nextR], [Bx, nextB])

            # 같은줄, 레드가 오른쪽에 있을때 →
            canR, canB = True, True
            nextR, nextB = Ry, By
            for i in range(M - 2):
                tmpRy = Ry + i
                if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                    if board[Rx][tmpRy] == 'O':
                        # Blue도 같이 빠지면 무효.
                        for j in range(M - 3):
                            tmpBy = By + j
                            if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                                if board[Bx][tmpBy] == 'O':
                                    return
                        result = cnt
                        return
                    nextR = tmpRy
                else:
                    canR = False

            # 잠시 막아두기
            board[Rx][nextR] = '#'
            for i in range(M - 3):
                tmpBy = By + i
                if canB and 0 < tmpBy < M - 1 and board[tmpBx][By] != '#':
                    if board[tmpBx][By] == 'O':
                        board[Rx][nextR] = '.'
                        return
                    nextB = tmpBy
                else:
                    canB = False

            board[Rx][nextR] = '.'
            rolling(cnt + 1, [Rx, nextR], [Bx, nextB])

    else:
        # ←
        canR, canB = True, True
        nextR, nextB = Ry, By
        for j in range(M-2):    # 범위가 1 ~ M-2 까지니까
            tmpRy = Ry - j
            tmpBy = By - j
            if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                if board[Rx][tmpRy] == 'O':
                    result = cnt
                    return
                nextR = tmpRy
            else:
                canR = False

            if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                if board[Bx][tmpBy] == 'O':
                    return
                nextB = tmpBy
            else:
                canB = False
        rolling(cnt + 1, [Rx, nextR], [Bx, nextB])

        # →
        canR, canB = True, True
        nextR, nextB = Ry, By
        for j in range(M-2):
            tmpRy = Ry + j
            tmpBy = By + j
            if canR and 0 < tmpRy < M - 1 and board[Rx][tmpRy] != '#':
                if board[Rx][tmpRy] == 'O':
                    result = cnt
                    return
                nextR = tmpRy
            else:
                canR = False

            if canB and 0 < tmpBy < M - 1 and board[Bx][tmpBy] != '#':
                if board[Bx][tmpBy] == 'O':
                    return
                nextB = tmpBy
            else:
                canB = False
        rolling(cnt + 1, [Rx, nextR], [Bx, nextB])


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
