# MooTube, 골드 5

def recommend_video(k, v):
    visited = [0 for i in range(N+1)]
    to_visit = [[v, 10**9]]

    while to_visit:
        x, u = to_visit.pop()
        if visited[x] == 0 and u >= k:
            visited[x] = 1
            to_visit.extend(usado_map[x])

    return sum(visited)-1


if __name__ == '__main__':
    N, Q = map(int, input().split(' '))
    INF = 100000

    usado_map = [[] for i in range(N+1)]

    for n in range(N-1):
        a, b, u = map(int, input().split(' '))
        usado_map[a].append([b, u])
        usado_map[b].append([a, u])

    result = list()
    for q in range(Q):
        k, v = map(int, input().split(' '))
        result.append(recommend_video(k, v))

    for res in result:
        print(res)