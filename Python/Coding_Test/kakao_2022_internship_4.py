import sys
sys.setrecursionlimit()


def min_of_intensity(graph, start, gates, summits):
    # start부터 각 노드에 도달하기까지 intensity 값 담기
    intensity = {node: 10**7 for node in graph}
    intensity[start] = 0
    queue = []
    queue.append([intensity[start], start])

    visited = list()

    while queue:
        cur_in, cur_node = queue.pop(0)

        for adj, w in graph[cur_node]:
            intensity[adj] = min(intensity[adj], max(w, cur_in))
            if adj in summits:
                continue
            elif adj in gates:
                continue
            elif adj not in visited:
                queue.append([intensity[adj], adj])
                visited.append(adj)

    res = [-1, 10**7]
    for s in summits:
        if intensity[s] < res[1]:
            res = [s, intensity[s]]

    print(start, intensity)
    return res


def solution(n, paths, gates, summits):
    answer = []
    res_min = 10 ** 7
    graph = dict()

    for i in range(len(paths)):
        a, b, w = paths[i]
        graph[a] = graph.get(a, [])
        graph[a].append([b, w])
        graph[b] = graph.get(b, [])
        graph[b].append([a, w])

    for i in range(len(gates)):
        tmp = min_of_intensity(graph, gates[i], gates, summits)

        if tmp[0] != -1 and tmp[1] < res_min:
            answer = tmp
            res_min = tmp[1]

    return answer


if __name__ == "__main__":
    print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
    # print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))