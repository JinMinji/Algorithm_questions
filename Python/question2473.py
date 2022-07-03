#세 용액, 골드3
import sys

def lower_bound(num, lst):  # num보다 작은 값을 가진 max 인덱스 반환
    start = 0
    end = len(lst) - 1
    tmp_res = 0
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < num:
            start = mid + 1
            tmp_res = mid

        else:
            end = mid - 1

    return tmp_res


def find_zero(i):
    global result, answer
    target = liquid_lst[i]

    left = 0
    right = N-1

    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1

        if abs(liquid_lst[left] + liquid_lst[right] + target) < result:
            answer = [liquid_lst[left], liquid_lst[right], target]
            # print(answer, sum(answer), result)
            result = abs(sum(answer))

        if left + right + target <= 0:
            left += 1

        else:
            right -= 1


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    liquid_lst = list(map(int, sys.stdin.readline().split()))

    liquid_lst.sort()

    result = abs(sum(liquid_lst[:3]))
    answer = liquid_lst[:3]

    # 다 알칼리성이거나, 다 산성일 때.
    if liquid_lst[0] > 0:
        # 작은 걸로 두개 뽑아주면 된당.
        print(answer)

    elif liquid_lst[-1] < 0:
        # 큰 걸로 두개 뽑아주면 된당.
        print(liquid_lst[-3:])

    else:
        for i in range(N):
            find_zero(i)
    answer.sort()
    print(*answer)

