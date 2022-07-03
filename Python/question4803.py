#4803 트리, 골드 4
import sys


def dfs(node, visited):
    global graph
    n_cnt, e_cnt = 1, len(graph[node])
    for next_node in graph[node]:
        if visited[next_node] == 0:
            visited[next_node] = 1
            n, e = dfs(next_node, visited)
            n_cnt += n
            e_cnt += e

    return n_cnt, e_cnt


if __name__ == "__main__":
    case = 1
    while True:
        n, m = map(int, sys.stdin.readline().split())

        if n == 0:
            break

        graph = [[] for i in range(n)]
        for i in range(m):
            a, b = map(int, sys.stdin.readline().split())
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        result = 0
        visited = [0 for i in range(n)]
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                n, e = dfs(i, visited)
                if n - 1 == e//2:
                    result += 1

        if result == 0:
            print("Case %d: No trees." %case)

        elif result == 1:
            print("Case %d: There is one tree." %case)

        else:
            print("Case %d: A forest of %d trees." %(case, result))

        case += 1