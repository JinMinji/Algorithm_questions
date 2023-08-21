# 20210825 보물상자

result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = 0, 0
dist_map = list()

def isPossible(x, y):
    return 0<=x<N*M and 0<=y<N*M

def BFS(graph, start):
    to_visit = list()
    visited = list()

    to_visit.append(start)
    while to_visit:
        node = to_visit.pop(0)
        i, j = node
        if node not in visited:
            visited.append(node)
            for _ in range(4):
                x = i + dx[_]
                y = j + dx[_]
                if isPossible(x, y) and graph[x][y] == 'L':
                    to_visit.append([x, y])



if __name__ == '__main__':
    N, M = map(int, input().split())

    treasure_map = list()

    for i in range(N):
        treasure_map.append(input())

    dist_map = [[N*M]