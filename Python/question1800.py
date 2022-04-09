# 인터넷 설치, 골드 1

def dijkstra(start):
    edge_cost[start][start] = 0

    for i in range(len(edge_cost[start])):
        

if __name__ == '__main__':
    N, P, K = map(int, input().split())
    INF = 10**10
    edge_cost = [[INF for i in range(P+1)] for i in range(P+1)]

    graph = dict()

    for i in range(P):
        a, b, cost = map(int, input())
        edge_cost[a][b] = cost
        edge_cost[b][a] = cost

        graph[a] = graph.get(a, {})
        graph[a][b] = cost
        graph[b] = graph.get(b, {})
        graph[b][a] = cost

    #dijkstra

    to_visit = list()

