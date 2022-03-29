# 사전, 골드 3 - 맞았습니다!
# 메모리 초과 해결을 위해, 순서만 먼저 체크하는 방법 사용

def solutions(N, M, K, cur_string):
    # N = 4, M = 2인 경우

    # aaaaz_    # 1C0 -> 1개 step 0 -> 남은 N = 0
    # aaaz__    # 2C1 -> 2개 step 1 -> 남은 N = 1
    # aaz___    # 3C2 -> 3개
    # az____    # 4C3 -> 4개
    # z_____    # 5C4 ->

    if N == 0:
        cur_string += 'z'*M
        return cur_string

    cur_total = 0
    step = 0
    for i in range(N+1):
        if cur_total + combination_cnt(M+i-1, i) >= K:
            step = i
            break
        cur_total += combination_cnt(M+i-1, i)

    cur_string += 'a'*(N-step)
    if M != 0:
        cur_string += 'z'
    return solutions(step, M-1, K-cur_total, cur_string)


def combination_cnt(n, r):
    res = 1
    if r == 0:
        return 1

    for i in range(1, n+1):
        res *= i

    tmp = 1
    for i in range(1, r+1):
        tmp *= i

    for i in range(1, n-r+1):
        tmp *= i

    return res//tmp


if __name__ == '__main__':
    N, M, K = map(int, input().split(' '))
    if combination_cnt(N+M, N) < K:
        print(-1)

    else:
        print(solutions(N, M, K, ''))
