#강의실 배정
import heapq

if __name__ == '__main__':
    N = int(input())

    lectures = list()

    for _ in range(N):
        s, e = map(int, input().split(' '))
        heapq.heappush(lectures, (s, e))

    result = list()

    while lectures:
        next_lec = list(heapq.heappop(lectures))
        # print(result, lectures, next_lec)
        if result and result[0] <= next_lec[0]:
            heapq.heappop(result)

        heapq.heappush(result, next_lec[1])     # 끝나는시간

    print(len(result))