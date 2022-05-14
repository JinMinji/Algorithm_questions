#컵라면, 골드 2
import heapq

if __name__ == "__main__":
    N = int(input())

    ramyeons = list()

    dead_lines = [[] for i in range(N+1)]
    for i in range(N):
        time, ra_num = map(int, input().split())
        dead_lines[time].append(ra_num)

    #연료채우기 문제와 같은 풀이
    #라면을 많이 주는 순으로 뽑아갈건데,
    #데드라인이 늦은 거 먼저 탐색!

    result = 0
    cur_heap = list()
    for i in range(N, 0, -1):
        if dead_lines[i]:
            for j in range(len(dead_lines[i])):
                heapq.heappush(cur_heap, -dead_lines[i][j])
        if cur_heap:
            result -= heapq.heappop(cur_heap)


    print(result)