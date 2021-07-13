#20210621 궁금한 민호
import copy

def floyd_warshall(graph):
    res_graph = copy.deepcopy(graph)
    for k in range(len(graph)): # 경유지
        for i in range(len(graph)):
            for j in range(len(graph)):
                res_graph[i][j] = min(res_graph[i][j], res_graph[i][k] + res_graph[k][j])

    return res_graph


def check_min(graph):
    answer = 0
    result = [[-1 for i in range(N)] for j in range(N)]

    for k in range(len(graph)):  # 경유지
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i == k or j == k or result[i][j] == 0:
                    continue
                elif graph[i][j] == graph[i][k]+graph[k][j]: # 경유지 지나서 가는게 더 이득임. = 필요없는 간선.
                    result[i][j] = 0
                elif graph[i][j] < graph[i][k]+graph[k][j]: # i -> j가 일단 필요한 간선일 수 있음
                    result[i][j] = graph[i][j]
                else: #graph[i][j] > graph[i][k]+graph[k][j]:   #잘못구함
                    return -1

    for i in range(N):
        for j in range(N):
            answer += result[i][j]

    return answer


if __name__ == '__main__':
    N = int(input())
    min_dist = list()
    for i in range(N):
        min_dist.append(list(map(int, input().split())))

    print(check_min(min_dist)//2)














