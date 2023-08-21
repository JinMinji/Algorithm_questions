#세부, 골드4
import sys
import heapq

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    s, e = map(int, sys.stdin.readline().split())

    #혜빈이 위치로 가는 경로에 속한 가장 작은 값이 가장 큰 경로 찾기.


    bridges = [[] for i in range(N)]
    for i in range(M):
        h1, h2, k = map(int, sys.stdin.readline().split())
        heapq.heappush(bridges[h1-1], [-k, h2-1])
        heapq.heappush(bridges[h2-1], [-k, h1-1])

    max_weight = [0 for i in range(N)]

    to_visit = [[s-1, 1_000_000]]
    max_weight[s-1] = 1_000_000

    while to_visit:
        cur, weight = to_visit.pop(0)
        for w, i in bridges[cur]:
            tmp_weight = min(weight, -w)
            if max_weight[i] < tmp_weight:
                max_weight[i] = tmp_weight
                to_visit.append([i, tmp_weight])


    print(max_weight[e-1])