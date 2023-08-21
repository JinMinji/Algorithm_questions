#2110, 공유기 설치, 골드 5
import sys


def is_possible(mid, houses, C):

    cur = houses[0]
    C -= 1      # 일단 맨 앞집에 설치.

    for i in range(1, len(houses)):
        if houses[i] >= cur+mid:
            cur = houses[i]
            C -= 1
            if C <= 0:
                return True

    return False


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().split())

    houses = []

    for i in range(N):
        houses.append(int(sys.stdin.readline().rstrip()))

    houses.sort()

    start = 0
    end = houses[-1]
    answer = start
    # print(start, end)
    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        if is_possible(mid, houses, C):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    print(answer)