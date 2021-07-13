#20210630 트리의 지름 2번째 풀이

def from_root(root):  # farthest from root node
    start = root
    dist = [-1 for _ in range(n+1)]
    dist[start] = 0
    to_visit = list()
    to_visit.append(start)

    while to_visit:
        node = to_visit.pop()   # 뒤에서부터 꺼낸다 -> LIFO
        if node in tree:
            for w, c in tree[node]:
                if c not in visited:
                    visited.append(c)
                    to_visit.append(c)
                    dist[c] = dist[node] + w
    max_dist = max(dist)
    far_node = dist.index(max_dist)

    return far_node

def from_node(node):
    tmp_visited = list()
    tmp_visited.append(node)
    dist = [-1 for _ in range(n + 1)]
    dist[node] = 0
    to_visit = list()
    to_visit.append(node)

    while to_visit:
        node = to_visit.pop()  # 뒤에서부터 꺼낸다 -> LIFO
        if node in graph:
            for w, c in graph[node]:
                if c not in tmp_visited:
                    tmp_visited.append(c)
                    to_visit.append(c)
                    dist[c] = dist[node] + w

    max_dist = max(dist)

    return max_dist



if __name__ == '__main__':
    n = int(input())

    tree = dict()
    graph = dict()
    for i in range(n-1):
        node, child, weight = map(int, input().split())

        tree[node] = tree.get(node, []) + [[weight, child]]
        graph[node] = graph.get(node, []) + [[weight, child]]
        graph[child] = graph.get(child, []) + [[weight, node]]

    visited = list()
    visited.append(1)   # root : 1
    node1 = from_root(1)

    print(from_node(node1))