# 승부 예측 골드 3


if __name__ == '__main__':
    nations = list(map(str, input().split(' ')))

    win_score = [0.0 for i in range(4)]

    for _ in range(6):
        A, B, W, D, L = input().split(' ')
        W = float(W)
        D = float(D)
        L = float(L)
        idx_A = nations.index(A)
        idx_B = nations.index(B)
        win_score[idx_A] += 3*W + D
        win_score[idx_B] += 3*L + D

        # print(win_score)

        # if W == 1.0:
        #     win_score[A] = win_score.get(A, 0) + 3
        # elif D == 1.0:
        #     win_score[A] = win_score.get(A, 0) + 1
        #     win_score[B] = win_score.get(B, 0) + 1
        # elif L == 1.0:
        #     win_score[B] = win_score.get(B, 0) + 3

    result = [0 for i in range(4)]
    check_idx = list()

    for i in range(len(win_score)):
        if win_score[i] == 9:
            result[i] = 1
        elif win_score[i] == 0:
            result[i] = 0
        else:
            check_idx.append(i)

    tmp_sum = 0
    for idx in check_idx:
        tmp_sum += win_score[idx]

    tmp_val = (2 - sum(result)) / tmp_sum

    for idx in check_idx:
        result[idx] = win_score[idx] * tmp_val

    for i in range(4):
        print(format(result[i], "0.6f"))
