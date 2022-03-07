#도시 분할 계획

edges = list()

# kruskal
parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    root1 = find(a)
    root2 = find(b)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(N, edges):
    mst = list()

    for node in range(1, N+1):
        make_set(node)

    for edge in edges:
        weight, a, b = edge
        if find(a) != find(b):
            union(a, b)
            mst.append(edge)

    return mst


if __name__ == '__main__':
    N, M = map(int, input().split(' '))

    edges = list()

    for _ in range(M):
        a, b, c = map(int, input().split(' '))
        edges.append([c, a, b])

    edges.sort()

    mst = kruskal(N, edges)
    mst.sort()

    result = 0
    for _ in range(len(mst)-1):
        result += mst[_][0]

    print(result)

