# 트리의 지름, 골드 3
# 트리의 지름은 임의의 노드에서 가장 멀리 떨어진 노드 a를 찾고, a노드에서 가장 멀리 떨어진 노드 b를 찾은 후
# a와 b 사이의 거리를 구하면 된답니다.
# 원대님 블로그 속 링크 참조 *^^*

import sys


def solutions(node):    # 가장 멀리있는 노드 반환하는 함수
    global answer

    to_visit = list()
    visited = [0 for i in range(len(tree))]
    to_visit.append([node, 0])
    visited[node] = 1
    max_cost = 0
    far_node = -1

    while to_visit:
        cur_node, cur_cost = to_visit.pop(0)
        for i in range(len(tree[cur_node])):
            next_node, next_cost = tree[cur_node][i]
            if visited[next_node] == 1:
                continue
            to_visit.append([next_node, next_cost + cur_cost])
            visited[next_node] = 1

            if next_cost + cur_cost > max_cost:
                max_cost = next_cost + cur_cost
                far_node = next_node

    answer = max_cost

    return far_node


if __name__ == '__main__':
    V = int(input())

    tree = [[] for i in range(V)]
    for v in range(V):
        tmp_str = list(map(int, sys.stdin.readline().split()))
        for i in range(1, len(tmp_str), 2):
            if tmp_str[i] == -1:
                break
            else:   #인덱스 0부터 시작할거라, -1 해줌
                tree[tmp_str[0]-1].append([tmp_str[i]-1, tmp_str[i+1]])

    answer = 0

    a = solutions(0)
    b = solutions(a)

    print(answer)

