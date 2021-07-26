#20210719 민준이와 마산 그리고 건우
import heapq


def dijkstra(graph, start):
    max_default = len(graph)*10000
    min_list = [max_default for i in range(len(graph)+1)]
    min_list[start] = 0

    tmp_queue = list()

    heapq.heappush(tmp_queue, [min_list[start], start])
    while tmp_queue:
        cur_dist, cur_node = heapq.heappop(tmp_queue)
        if min_list[cur_node] < cur_dist:
            continue

        for weight, adj in graph[cur_node]:
            dist = cur_dist + weight

            if dist < min_list[adj]:
                min_list[adj] = dist
                heapq.heappush(tmp_queue, [min_list[adj], adj])

    return min_list


if __name__ == '__main__':
    V, E, P = map(int, input().split())

    edges = [[] for i in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        heapq.heappush(edges[s], [w, e])
        heapq.heappush(edges[e], [w, s])

    # 출발은 1, 도착은 V
    min_dist_from_1 = dijkstra(edges, 1)
    min_dist_from_P = dijkstra(edges, P)

    if min_dist_from_1[V] == min_dist_from_1[P] + min_dist_from_P[V]:
        print("SAVE HIM")

    else:
        print("GOOD BYE")