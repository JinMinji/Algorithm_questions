# 우주신과의 교감, 골드3
import sys
import heapq
import math


def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    p1 = find(u)
    p2 = find(v)
    parent[p2] = p1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    connect = list()
    parent = [i for i in range(N + 1)]  # 부모리스트, 자기 자신으로 초기화

    universe_gods = list()
    for i in range(N):
        universe_gods.append(list(map(int, sys.stdin.readline().split())))

    for i in range(N):
        for j in range(i + 1, N):
            a_x, a_y = universe_gods[i]
            b_x, b_y = universe_gods[j]
            heapq.heappush(connect, [math.sqrt(abs(a_x - b_x) ** 2 + abs(a_y - b_y) ** 2), i, j])

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        union(a - 1, b - 1)

    edge_n = M  # 간선의 개수
    total_cost = 0  # 비용의 합
    while True:
        if edge_n == N - 1:
            break
        if not connect:
            break
        c, a, b = heapq.heappop(connect)
        if find(a) != find(b):
            total_cost += c
            edge_n += 1
            union(a, b)

    print('%.2f' % total_cost)
