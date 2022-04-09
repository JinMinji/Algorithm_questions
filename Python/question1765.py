# 닭싸움, 골드 1

def find(x):
    if leader[x] == x:
        return x
    else:
        return find(leader[x])


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    # 최대로 만들 수 있는 팀의 개수를 구하는 것이므로, 잘게 쪼갤 수록 좋음.

    friend_graph = [[] for i in range(n+1)]
    enemy_graph = [[] for i in range(n+1)]

    leader = [i for i in range(n+1)]

    for i in range(m):
        R, p, q = map(str, input().split())
        p = int(p)
        q = int(q)
        if R == 'F':
            friend_graph[p].append(q)
            friend_graph[q].append(p)
        else:
            enemy_graph[p].append(q)
            enemy_graph[q].append(p)

    for i in range(n):
        for f in friend_graph[i]:
            if leader[f] != leader[i]:
                root_i = find(i)
                leader[f] = root_i
                leader[i] = root_i

        for e in enemy_graph[i]:    # 원수 리스트를 돌면서,
            for ee in enemy_graph[e]:   # 원수의 원수는 나와 친구.
                if leader[ee] != leader[i]:
                    root_i = find(i)
                    leader[ee] = root_i
                    leader[i] = root_i
        # print(i, leader)

    answer = list()

    for i in range(1, len(leader)):
        if leader[i] not in answer:
            answer.append(leader[i])

    print(len(answer))

