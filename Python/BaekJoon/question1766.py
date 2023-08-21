# 위상 정렬. 난이도 중
# 힙 = 우선순위큐

import heapq

question_num, info = map(int,input().split())

edges = [[] for i in range(question_num+1)] # 각 노드마다, 나가는 엣지가 어디로 가는 지 담을 리스트 n개 초기화
indegrees = [0] * question_num # 각 노드의 진입차수를 담을 리스트 n개 0으로 초기화

for i in range(info):
    a, b = map(int, input().split())
    edges[a-1].append(b)
    indegrees[a-1] += 1

# n개 다 풀어야한다.
# 먼저나온 문제는 먼저푸는게 좋다.
# 먼저풀어야하는 문제 고려

result = list()
heap = list()

#먼저 차수가 0인 노드를 heap에 순서대로 넣어준다.
for i in range(question_num):
    if indegrees[i] == 0:
        heapq.heappush(heap, i+1)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in edges[data+1]:
        indegrees[y] -= 1
        if indegrees[y] == 0:
            heapq.heappush(heap, y+1)

for i in result:
    print(i, end=' ')




