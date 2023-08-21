#최소비용 구하기 2, 골드3
import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: [float('inf'), -1] for node in range(1, n+1)}
    distances[start] = [0, start]
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distinfo, current_node = heapq.heappop(queue)
        current_distance = current_distinfo[0]

        if distances[current_node][0] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent][0] = distance
                distances[adjacent][1] = current_node
                heapq.heappush(queue, [distances[adjacent], adjacent])

    return distances


if __name__ == "__main__":
    global n
    n = int(input())    # city, max 1000

    m = int(input())    # bus, max 10000

    graph = defaultdict(dict)

    for i in range(m):
        start, end, cost = map(int, input().split())
        graph[start][end] = min(graph[start].get(end, 10**5), cost)

    s_city, e_city = map(int, input().split())

    # s기준 다익스트라 돌면서,, 경로 기록해두고
    # e에서의 경로 출력.
    # 최소비용, 도시 개수, 도시 순서대로 출력

    answer = dijkstra(graph, s_city)

    # print(answer)
    print(answer[e_city][0])
    shortest_route = list()
    cur = e_city
    while True:
        shortest_route.append(cur)
        if cur == s_city:
            break

        else:
            cur = answer[cur][1]

    shortest_route.reverse()

    print(len(shortest_route))
    print(*shortest_route)