#20210621 궁금한 민호
import copy
import heapq

def floyd_warshall(graph):
    res_graph = copy.deepcopy(graph)
    for k in range(len(res_graph)): # 경유지
        for i in range(len(res_graph)):
            for j in range(len(res_graph)):
                res_graph[i][j] = min(res_graph[i][j], res_graph[i][k] + res_graph[k][j])

    return res_graph

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()

    for i in range(N):
        make_set(i)

    for edge in graph:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

if __name__ == '__main__':
    N = int(input())
    min_dist = list()
    for i in range(N):
        min_dist.append(list(map(int, input().split())))

    graph = list()
    for i in range(N):
        for j in range(N):
            heapq.heappush(graph, [min_dist[i][j], i, j])

    original_graph = kruskal(graph)

    result = 0
    for edge in original_graph:
        result += edge[0]

    print(result)











