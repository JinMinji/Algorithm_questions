import heapq


# 점 3개를 고를 때
# 점 하나를 고르고, 그 점에서의 최장거리가 점 두개를 고르면 됨.

def max_distance(n, edges, start):
    # 최장 거리 점을 두개 뽑기위해 모든 노드에 대한 거리를 구한다
    # 250000??

    distance = {i: 0 for i in range(1, n + 1)}
    print(distance)

    for edge in edges:
        pass

def solution(n, edges):
    answer = 0
    for i in range(n):
        max_distance(n, egdes, i)
        # answer = max(answer, max)

    return answer


solution(4, [[1,2],[2,3],[3,4]])