# 20210601 프로그래머스 이분탐색
# 징검다리 Level4

def solution(distance, rocks, n):
    answer = 0

    start = 0
    end = distance

    rocks.sort()

    while start <= end:
        mid = (start + end) // 2
        pre = 0
        d_rock_num = 0
        for r in rocks:
            if r - pre >= mid:
                pre = r
            elif d_rock_num < n:
                d_rock_num += 1
            else:
                end = mid - 1
                d_rock_num = -1
                break

        if d_rock_num >= 0:
            start = mid + 1
            answer = mid

    return answer

if __name__ == '__main__':
    print(solution(25, [2,14,11,21,17],2))