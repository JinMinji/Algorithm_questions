# 20210630 양구출작전 2번째 풀이

def find_leaf():
    leaf = list()
    for i in range(2, N+1):
        if len(island_back[i]) == 0:
            leaf.append(i)
    return leaf


def save_sheep(leaf):
    now = leaf
    now_sheep = 0
    while len(island_map[now]) > 0:
        tmp = now_sheep + island_map[now][0]
        now_sheep = max(0, now_sheep + island_map[now][0])  # -면, 0으로 바꿔줘야함.
        island_map[now][0] = min(0, island_map[now][0])  # +면, 데리고 갈거니까 0으로 바꿔줘야함.

        now = island_map[now][1]

    if now != 1:
        return 0

    return now_sheep


if __name__ == '__main__':
    N = int(input())

    island_map = [[] for i in range(N + 1)]
    island_back = [[] for i in range(N + 1)]
    for i in range(2, N + 1):
        t, n, adj = input().split()
        if t == 'W':
            island_map[i] = [-int(n), int(adj)]
        else:
            island_map[i] = [int(n), int(adj)]
        #     island_map[i] = [t, int(n), int(adj)]
        island_back[int(adj)].append(i)

    leaf = find_leaf()

    answer = 0

    for i in leaf:
        answer += save_sheep(i)

    print(answer)