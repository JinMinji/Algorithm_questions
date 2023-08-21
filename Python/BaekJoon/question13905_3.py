#세부, 골드4
import sys
import heapq


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    p1 = find(a)
    p2 = find(b)

    if p1 != p2:
        parent[b] = a


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    s, e = map(int, sys.stdin.readline().split())

    #혜빈이 위치로 가는 경로에 속한 가장 작은 값이 가장 큰 경로 찾기.
    parent = [i for i in range(N+1)]
    bridges = []

    for i in range(M):
        h1, h2, k = map(int, sys.stdin.readline().split())
        heapq.heappush(bridges, [-k, h1, h2])   #가능한 무게가 큰 순서로 넣을 것이므로, -k

    cnt = 0
    result = 1_000_000

    while cnt < N and s != e:  # N개의 섬을 연결하려면, N-1개의 다리가 필요.
        # 싸이클 없이 만들것이므로, N-1개 이상은 필요없음.
        # 더 이상 확인해볼 다리가 없거나,

        w, a, b = heapq.heappop(bridges)
        # 이동 가능한 무게가 큰 순서대로 뽑아서,
        if find(a) != find(b):  # 연결되지 않은 지점이면
            # 현재 무게 w가 지금까지 연결한 다리의 무게제한 중 가장 작은 무게일 것이므로!
            result = -w
            print(result)
            # result 를 w로 갱신(-k로 넣어줬으므로 -w해준다.)
            cnt += 1
            # 연결한 다리개수 += 1
            union(a, b)
            # 두 지점 union처리

        if find(s) == find(e):
            break

    if find(s) == find(e):
        print(result)
    else:
        print(0)