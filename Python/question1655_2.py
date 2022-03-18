# 가운데를 말해요 골드 2
import sys
import heapq

if __name__ == '__main__':
    N = int(input())

    left_num_l = list()
    right_num_l = list()
    answer = list()

    for i in range(N):
        n = int(sys.stdin.readline())
        if len(left_num_l) == len(right_num_l):
            heapq.heappush(left_num_l, (-n, n))

        else:
            heapq.heappush(right_num_l, (n, n))

        if right_num_l and left_num_l[0][1] > right_num_l[0][1]:
            l_max = heapq.heappop(left_num_l)[1]
            r_min = heapq.heappop(right_num_l)[1]
            heapq.heappush(left_num_l, (-r_min, r_min))
            heapq.heappush(right_num_l, (l_max, l_max))

        answer.append(left_num_l[0][1])

    for _ in range(len(answer)):
        print(answer[_])