# 우수 마을, 골드 3

def good_village(node):
    visited = [0 for i in range(N+1)]

    for i in range(len(graph[node])):
        child = graph[node][i]
        if visited[child] == 1:
            continue


if __name__ == '__main__':
    N = int(input())

    member = list(map(int, input().split(' ')))

    graph = [[] for i in range(N + 1)]

    for i in range(N-1):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    dp = [[0, 0] for i in range(N+1)]
    # dp[n][1] : n이 우수마을일 때 최댓값
    # dp[n][0] : n이 우사마을이 아닐 때 최댓값

    good_village(1, 0)

    print(max(dp[1][0], dp[1][1]))