#20210615 백양로브레이크
import copy

def floyd_warshall(graph):
    min_cost = copy.deepcopy(graph)

    for k in range(len(graph)): # 경유지
        for i in range(len(graph)):
            for j in range(len(graph)):
                min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

    return min_cost


if __name__ == '__main__':
    n, m = map(int, input().split())

    MAX = n*n
    roads = [[MAX for i in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        roads[i][i] = 0
    # A건물 to A건물은 바꿀 필요 없으니까.

    for i in range(m):
        p1, p2, bi = map(int, input().split())
        roads[p1][p2] = 0
        if bi == 0:
            roads[p2][p1] = 1
        else :
            roads[p2][p1] = 0

    result = floyd_warshall(roads)

    k = int(input())
    answers = list()

    for i in range(k):
        s, e = map(int, input().split())
        answers.append(result[s][e])

    for i in range(k):
        print(answers[i])

    # 딕셔너리로 하는 방법?
    # roads = dict()
    #
    # for i in range(m):
    #     x1, x2, bi = map(int, input().split())
    #     roads[x1] = roads.get(x1, []) + [x2]
    #     if bi == 1:
    #         roads[x2] = roads.get(x2, []) + [x1]