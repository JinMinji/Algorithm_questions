#16938, 캠프준비, 골드 5
import sys


if __name__ == "__main__":
    N, L, R, X = map(int, sys.stdin.readline().split())
    difficulties = list(map(int, sys.stdin.readline().split()))

    difficulties.sort()
    # print(difficulties)
    result = 0
    test_print = list()
    for i in range(1, 2**N):    #아무것도 고르지않는 경우는 빼야하므로 1부터 시작한다. 1 ~ (2**N)-1
        min_d = 10**6
        max_d = 0
        total = 0
        tmp = str(bin(i))
        # print(tmp)
        for i in range(1, len(tmp)-1):
            # print(i, tmp[-i], difficulties[-i])
            if tmp[-i] == '1':
                total += difficulties[-i]
                min_d = min(min_d, difficulties[-i])
                max_d = max(max_d, difficulties[-i])

        if max_d - min_d >= X and L <= total <= R:
            result += 1
            # test_print.append(tmp)
    # print(test_print)
    print(result)