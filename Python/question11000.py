#강의실 배정
import heapq

if __name__ == '__main__':
    N = int(input())

    lectures = list()

    for _ in range(N):
        heapq.heappush(lectures, (map(int, input().split(' '))))

    result = list()
    cur_time = 0

    while lectures:
        next_lec = heapq.heappush(lectures)
        if result