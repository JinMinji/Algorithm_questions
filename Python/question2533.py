# 20210628 사회망 서비스(SNS)
early_min = list()

def min_early_adopter(graph, node):
    early = 1
    not_early = 0

    for c in graph.get(node, []):
        # 내가 얼리일때 early
        # 1. 내 자식이 얼리 일수도, 아닐 수도 있음

        if early_min[c][1] == N:    #하나만 체크
            early_min[c] = min_early_adopter(graph, c)

        early += min(early_min[c])

        # 내가 얼리가 아닐 때 not_early
        # 1. 내 자식이 모두 얼리여야함
        not_early += early_min[c][1]

    early_min[node] = [not_early, early]
    return[not_early, early]

if __name__ == '__main__':
    N = int(input())

    friend_graph = dict()
    for i in range(N-1):
        node1, node2 = map(int, input().split())
        friend_graph[node1] = friend_graph.get(node1, []) + [node2]
        #friend_graph[node2] = friend_graph.get(node2, []) + [node1]
    # 값이 작은 것부터 입력되므로, 작은게 부모, 뒤에 오는게 자식인걸로 해서 단방향트리로 입력받기.

    early_min = [[N, N] for i in range(N + 1)]
    # early_min[x][0] : 내가 Early Adopter일 때의 최소값
    # early_min[x][1] : 내가 Early Adopter가 아닐 때의 최소값

    min_early_adopter(friend_graph, 1)

    print(min(early_min[1]))

