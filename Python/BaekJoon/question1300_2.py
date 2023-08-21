#백준 1300, K번째 수

def upper_bound(n, k, num):
    temp_res = 0
    for i in range(1, n+1):
        temp_res += min(num/i, n)

        if temp_res >= k:
            return True

    return False


def solutions(n, k):
    start = 1
    end = k

    result = start

    while start < end:
        mid = (start + end) // 2

        if upper_bound(n, k, mid):
            # mid가 배열에 속한 숫자인지도 확인을 해야함.
            for i in range(1, n+1):
                if mid % i == 0 and mid // i <= n:
                    result = mid

                end = mid - 1

        else:
            start = mid + 1

    return result


if __name__ == '__main__':
    n = int(input())
    k = int(input())

    print(solutions(n, k))