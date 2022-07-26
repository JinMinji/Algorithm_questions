#13023, ABCDE, 골드5
import sys


def dfs(cur, cnt, route):
    # print(route, cur)
    global result, visited, to_visit

    root = route[0]
    if len(visited[root]) < cnt:
        visited[root] = route

    if result == 1 or cnt >= 5:
        result = 1
        return
    elif cur != -1:
        for f in friends[cur]:
            if visited[f] and cur not in visited[f] and root not in visited[f]:
                dfs(-1, cnt+len(visited[f]), route+visited[f])
            elif f not in route:
                dfs(f, cnt+1, route + [f])


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    friends = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        friends[a].append(b)
        friends[b].append(a)

    # 0번 사람의 친구부터 탐색해 나간다. 깊이가 5이상이면 result = 1
    result = 0
    visited = [[] for i in range(N)]
    for i in range(N):
        visited[i] = [i]
        dfs(i, 1, [i])

    # print(visited)
    print(result)