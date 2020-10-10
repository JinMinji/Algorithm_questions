#최소힙
import heapq
case_num = int(input())
min_heap = list()
result = list()

for i in range(case_num):
    val = int(input())
    if val == 0:
        if min_heap:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)

    else:
        heapq.heappush(min_heap, val)

for i in result:
    print(i)


#어이없게 pypy3으로 제출해야 맞음;