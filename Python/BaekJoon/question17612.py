#쇼핑몰, 골드2
import sys
import heapq


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())

    counter = list()
    for i in range(K):
        heapq.heappush(counter, [0, i]) #처음에는 앞번호 카운터 먼저 배정하고,

    result = list()
    customers = list()
    for i in range(N):
        time, c_idx = heapq.heappop(counter)
        mem_id, t = map(int, sys.stdin.readline().split())
        heapq.heappush(counter, [time+t, c_idx])
        heapq.heappush(result, [time+t, -c_idx, mem_id])

    answer = 0
    for i in range(len(result)):
        a, b, c = heapq.heappop(result)
        answer += c*(i+1)

    # print(result)
    print(answer)