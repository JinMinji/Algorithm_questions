# 20210628 트리의 지름
import heapq

def find_far_node(start):       # 루트에서 제일 먼 거리를 가진 노드 찾기, 결과값의 한 쪽이 될 노드.
    to_visit = list()
    to_visit.append(start)
    far_node = 0
    weight_list = []
    result_max = 0

    while to_visit:
        node = to_visit.pop()   # DFS 이므로 뒤에서부터 꺼냄.

        if not tree.get(node, []):    # 리프노드
            weight_list.pop()

        else:
            to_visit.append(node)
            for c_weight, c in tree[node]:
                if c not in visited:
                    visited.append(c)
                    if result_max < sum(weight_list) + c_weight:
                        result_max = sum(weight_list) + c_weight
                        far_node = c

                    weight_list.append(c_weight)
                    to_visit.append(c)
                    print(c, weight_list, to_visit)

                else:   # 자식들을 다 방문함, 위로 돌아가는 중일 때
                    if weight_list:
                        weight_list.pop()
                    if to_visit:
                        to_visit.pop()
                    break
    print("max_dist : ", result_max)
    return far_node

def find_max_to_max(max_node):
    to_visit = list()
    to_visit.append(max_node)
    weight_list = []
    max_weight = 0

    while to_visit:
        node = to_visit.pop()

        for c_weight, c in graph[node]:
            is_final = True
            if c not in visited:
                is_final = False
                to_visit.append(c)
                weight_list.append(c_weight)
                max_weight = max(max_weight, sum(weight_list))

            if is_final:
                weight_list.pop()

    return max_weight


if __name__ == '__main__':
    n = int(input())

    tree = dict()
    graph = dict()
    for i in range(n-1):
        node, child, weight = map(int, input().split())
        # tmp = tree.get(node, [])
        # heapq.heappush(tmp, [weight, child])
        # tree[node] = tmp

        tree[node] = tree.get(node, []) + [[weight, child]]
        graph[node] = graph.get(node, []) + [[weight, child]]
        graph[child] = graph.get(child, []) + [[weight, node]]

    print(tree)

    # 루트는 1, 1부터 탐색한다.
    visited = list()
    visited.append(1)
    max_node = find_far_node(1)
    visited = list()    # visited reset

    print(max_node)
    # print(find_max_to_max(max_node))