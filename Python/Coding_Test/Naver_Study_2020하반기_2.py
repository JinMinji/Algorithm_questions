# 트리 간선제거
from itertools import combinations
import copy


def isCorrect(graph, n):
    target = n//3
    visited = [0 for i in range(n)]
    to_visit = list()
    visited[0] = 1
    to_visit.extend(graph[0])

    cnt = 1
    while to_visit:
        node = to_visit.pop(0)
        if visited[node] == 0:  #방문한 적 없음.
            visited[node] = 1   #방문체크
            cnt += 1            #개수 + 1
            to_visit.extend(graph[node])

    if cnt != target:
        return False

    next_start = 0
    for i in range(n):
        if visited[i] == 0:
            next_start = i

    to_visit = []
    visited[next_start] = 1
    to_visit.extend(graph[next_start])
    cnt = 1

    while to_visit:
        node = to_visit.pop(0)
        if visited[node] == 0:  # 방문한 적 없음.
            visited[node] = 1  # 방문체크
            cnt += 1  # 개수 + 1
            to_visit.extend(graph[node])

    if cnt != target:
        return False

    else:
        return True


def solutions(n, edges):
    answer = 0
    graph = dict()
    for i in range(len(edges)):
        a, b = edges[i]
        graph[a] = graph.get(a, [])
        graph[a].append(b)
        graph[b] = graph.get(b, [])
        graph[b].append(a)

    # edge 최대가 98. 98C2 -> 4753
    tmp = [i for i in range(n-1)]
    temp_list = list(combinations(tmp, 2))
    for i in range(len(temp_list)):
        a, b = temp_list[i]
        temp_graph = copy.deepcopy(graph)
        temp_graph[edges[a][0]].remove(edges[a][1])
        temp_graph[edges[a][1]].remove(edges[a][0])
        temp_graph[edges[b][0]].remove(edges[b][1])
        temp_graph[edges[b][1]].remove(edges[b][0])

        if isCorrect(temp_graph, n):
            answer = temp_list[i]   # 정답은 한개뿐.
            break

    return answer


if __name__ == '__main__':
    print(solutions(9, [[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]))