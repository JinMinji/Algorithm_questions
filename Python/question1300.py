#백준 1300, K번째 수

def upper_bound(n, k, num):
    temp_res = 0
    for i in range(1, n+1):
        temp_res += min(num//i, n)

        if temp_res >= k:
            return True

    return False


def solutions(n, k):
    start = 1
    end = k

    result = start

    while start <= end:
        mid = (start + end) // 2

        if upper_bound(n, k, mid):
            result = mid
            end = mid - 1

        else:
            start = mid + 1

    # temp_res = k
    # # 없는 수가 정답으로 나올 수도 있다.
    # for i in range(1, n+1//2):
    #     for j in range(1, n+1):
    #         if i*j >= result:
    #             temp_res = min(temp_res, i*j)
    #             break
    #
    # return temp_res

    return result


if __name__ == '__main__':
    n = int(input())
    k = int(input())

    print(solutions(n, k))