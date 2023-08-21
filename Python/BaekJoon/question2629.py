# 양팔저울, 골드3
import sys


def solutions(idx, left, right):
    # print(idx, left, right, abs(left-right))

    if dp[abs(left-right)][idx]:
        return

    dp[abs(left - right)][idx] = True
    dp[left][idx] = True
    dp[right][idx] = True

    is_possible[left] = True
    is_possible[right] = True
    is_possible[abs(left - right)] = True

    if idx >= N:
        return

    solutions(idx + 1, left, right)
    solutions(idx + 1, left + weights[idx], right)
    solutions(idx + 1, left, right + weights[idx])


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    weights = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())

    marbles = list(map(int, sys.stdin.readline().split()))
    is_possible = dict()
    dp = [[False for i in range(N+1)] for i in range(N*500+1)]
    result = list()
    solutions(0, 0, 0)

    for i in range(M):
        if is_possible.get(marbles[i], False):
            result.append('Y')
        else:
            result.append('N')

    print(*result)