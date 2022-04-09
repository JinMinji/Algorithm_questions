# 송전탑, A->B까지 가중치가 K 미만인 경로에 포함되는 간선만 남기기. 남은 간선의 개수 리턴

def find(route, k, b):
    x = route[-1]
    if len(route) > k:
        return

    if x == b:
        for i in range(1, len(route)):
            if [route[i - 1], route[i]] in tmp_edges:  # or [route[i], route[i-1]] in edges:
                tmp_idx = tmp_edges.index([route[i - 1], route[i]])
                used_edges[tmp_idx] = 1
        return

    for _ in range(len(graph[x])):
        route.append(graph[x][_])
        find(route, k, b)
        route.pop()


def solution(n, edges, k, a, b):
    global answer, tmp_edges, used_edges, graph
    tmp_edges = edges

    used_edges = [0 for i in range(len(edges))]

    graph = [[] for i in range(n)]

    for e in range(len(edges)):
        node_1 = edges[e][0]
        node_2 = edges[e][1]
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    to_visit = list()
    to_visit.extend(graph[a])

    answer = 0
    while to_visit:
        x = to_visit.pop()
        find([a, x], k, b)

    return answer


if __name__ == '__main__':
    print(solution(8, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3 ))