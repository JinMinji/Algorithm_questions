#20210525 행성터널
parent = dict()
rank = dict()

def find(node): # 루트노드 찾기
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root_v = find(node_v)
    root_u = find(node_u)

    if rank[root_v] > rank[root_u]:
        parent[root_u] = root_v
    else:
        parent[root_v] = root_u
        if rank[root_v] > rank[root_u]:
            rank[root_v] += 1

def kruskal(graph):
    result = 0
    graph.sort(key=lambda x: x[0])  # 비용 기준 정렬

    for vertex in range(N):  # 초기화
        parent[vertex] = vertex
        rank[vertex] = 0

    for edge in graph:
        cost, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            result += cost

    return result

def min_cost():
    # x좌표, y좌표, z좌표 기준으로 각각 정렬해서 간선 구하고, 크루스칼 돌리기
    edges = list()
    for i in range(3):
        planets.sort(key=lambda x:x[i]) # x, y, z 기준으로 정렬
        for k in range(len(planets)-1):
            edges.append([abs(planets[k][i]-planets[k+1][i]), planets[k][3], planets[k+1][3]])
            #양쪽으로 다 넣어주기

    # 크루스칼(Kruskal)
    return kruskal(edges)

if __name__ == '__main__':
    N = int(input())

    planets = list()
    for i in range(N):
        tmp_list = list(map(int, input().split(" ")))
        tmp_list.append(i)  # 간선을 만들어주기 위해, 행성을 구분할 인덱스를 추가해준다.
        planets.append(tmp_list)

    print(min_cost())