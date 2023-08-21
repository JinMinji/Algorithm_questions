#20210605 가장 가까운 공통 조상

def find_common_ancestor(v1, v2, graph):
    ancestor = list()
    find1 = v1
    find2 = v2
    while(find1 != 0 or find2 != 0):
        if find1 != 0:      # 루트까지 탐색이 끝나면, find는 0
            if find1 in ancestor:
                return find1    #현
            else:
                ancestor.append(find1)
                if len(graph.get(find1, [])) != 0:
                    find1 = graph[find1].pop(0)
                else:
                    find1 = 0

        if find2 != 0:
            if find2 in ancestor:
                return find2
            else:
                ancestor.append(find2)
                if len(graph.get(find2, [])) != 0:
                    find2 = graph[find2].pop(0)
                else:
                    find2 = 0

    return 0

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        edges = dict()
        N = int(input())
        for j in range(N-1):        # 간선의 개수는 노드개수-1
            tmp_v1, tmp_v2 = map(int, input().split(" "))
            #edges[tmp_v1] = edges.get(tmp_v1, []) + [tmp_v2]        # 부모 -> 자식
            edges[tmp_v2] = edges.get(tmp_v2, []) + [tmp_v1]       # 자식 -> 부모

        vertex1, vertex2 = map(int, input().split(" "))

        print(find_common_ancestor(vertex1, vertex2, edges))
