#입국심사
desks = list()
N, M = 0, 0


def is_possible(time):
    tmp_mem = M
    for _ in range(N):
        tmp_mem -= (time//desks[_])
        if tmp_mem <= 0:
            return True

    return False


if __name__ == '__main__':
    N, M = map(int, input().split(' '))

    desks = list()

    for i in range(N):
        desks.append(int(input()))

    # 일단 비는대로 줄서서 하다가, 마지막에만 비교하자.

    start = 0
    end = M*(min(desks))   # Max

    result = end

    while start <= end:
        mid = (start + end) // 2

        if is_possible(mid):
            end = mid - 1
            result = mid

        else:
            start = mid + 1

    print(result)