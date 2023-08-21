# 뉴스 전하기, 골드 1
import heapq

if __name__ == '__main__':
    N = int(input())

    seniors = list(map(int, input().split()))

    tree = [[] for i in range(N)]
    children = [0 for i in range(N)]

    for i in range(1, len(seniors)):
        tree[seniors[i]].append(i)

    for i in range(len(seniors)-1, -1, -1):
        if not tree[i]:
            cur_total = 1
            parent = i
            while parent != -1:
                parent = seniors[parent]
                children[parent] += cur_total
                cur_total += 1

    print(tree)
    print(children)
    # 밑에 연결된 children 개수를 고려하되,
    # 동시에 여러명이 전화할 수 있으므로 여러갈래로 퍼트리는 게 이득.
    # rank가 높아야 이득.

    to_call = list()

    for i in range(len(tree[0])):
        heapq.heappush(to_call, [children[tree[0][i]], tree[0][i]])

    result = 0

    while to_call:
        tmp_x = heapq.heappop(to_call)
        result += 1

        x = tmp_x[1]
        for i in range(len(tree[x])):
            heapq.heappush(to_call, [children[tree[x][i]], tree[x][i]])

    print(result)