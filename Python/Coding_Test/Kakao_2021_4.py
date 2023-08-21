# 합승택시요금

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


def solution(n, s, a, b, fares):
    answer = 0

    graph = dict()
    for i in range(len(fares)):
        graph[fares[i][0]] = graph.get(fares[i][0], {})
        graph[fares[i][0]][fares[i][1]] = fares[i][2]

        graph[fares[i][1]] = graph.get(fares[i][1], {})
        graph[fares[i][1]][fares[i][0]] = fares[i][2]

    from_s = dijkstra(graph, s)
    from_a = dijkstra(graph, a)
    from_b = dijkstra(graph, b)

    answer = min(from_s[a]+from_a[b], from_s[b]+from_b[a])

    answer = min(answer, from_s[a]+from_s[b])

    return answer


if __name__ == '__main__':
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
