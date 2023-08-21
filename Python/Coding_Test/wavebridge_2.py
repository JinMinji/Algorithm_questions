def bin_search(lst, num):
    start = 0
    end = len(lst) - 1

    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] <= num:
            answer = mid
            start = mid + 1

        else:
            end = mid - 1

    return answer


def solution(M, load):
    answer = 0
    load.sort()
    if load[-1] > M:  # 가장 큰 물건의 무게가 트럭의 실을 수 있는 최대 무게 이상일 경우, 운반 불가.
        answer = -1

    else:
        # 가장 M에 근접한 무게로 가득 가득 실어야 최소 트럭의 개수로 옮길 수 있다. -> 그리디
        # 물건의 개수는 12개 미만이므로, 복잡도를 크게 고려하지 않아도 되지만, 효율성 문제임

        # 1. 이분탐색 풀이
        # cur = M
        # answer += 1
        # while load:
        #     tmp = bin_search(load, cur)
        #     # print(tmp, load[tmp])
        #     if tmp != -1:
        #         cur -= load.pop(tmp)
        #     else:
        #         answer += 1
        #         cur = M

        # # 한트럭에 두개이상 못싣나?
        # while load:
        #     answer += 1
        #     cur = M-load.pop()
        #     tmp = bin_search(load, cur)
        #     if tmp != -1:
        #         cur -= load.pop(tmp)

        # 2. 투포인터 풀이
        left = 0
        right = len(load) - 1
        if right == 0:
            answer = 1

        while left <= right:
            answer += 1
            if load[right] + load[left] <= M:
                left += 1
                right -= 1

            else:
                right -= 1

    return answer