# 트리의 부모 찾기

if __name__ == '__main__':
    N = int(input())

    graph = dict()

    for i in range(N-1):
        a, b = map(int, input().split(' '))
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    # 루트는 1이므로 1과 연결된 노드를 먼저 찾는다.
    to_visit = [1]

    result = [0 for i in range(N+1)]

    while to_visit:
        cur = to_visit.pop(0)
        for i in range(len(graph[cur])):
            next_node = graph[cur][i]
            if result[next_node] == 0:  # 방문한 적이 없을 때만! 안그러면 자식번호가 덮어씌워짐
                result[next_node] = cur
                to_visit.append(next_node)

    for i in range(2, N+1):
        print(result[i])
