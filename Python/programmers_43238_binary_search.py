# 20210601 프로그래머스 이분탐색
# 입국심사 Level3

def solution(n, times):
    answer = 0

    start = 0
    end = n * min(times)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                answer = mid
                end = mid - 1
                break

        if cnt < n:
            start = mid + 1

    return answer