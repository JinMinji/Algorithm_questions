# 인터넷 설치, 골드 1
import heapq

import heapq


# 탐색할 그래프와 시작 정점을 인수로 전달받습니다.
def dijkstra(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화합니다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])

    while queue:

        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트합니다.
        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = list()
    path_output.append(end)
    while distances[path][1] != start:
        path_output.append(distances[path][1])
        path = distances[path][1]
    path_output.append(start)
    print(path_output)
    return distances


if __name__ == '__main__':
    N, P, K = map(int, input().split())
    INF = 10 ** 10

    graph = dict()

    for i in range(P):
        a, b, cost = map(int, input().split())
        graph[a] = graph.get(a, {})
        graph[a][b] = cost
        graph[b] = graph.get(b, {})
        graph[b][a] = cost

    # dijkstra

    dijkstra(graph, 1, N)

