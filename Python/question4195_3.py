# 친구 네트워크

def union(a, b):
    r1 = find(a)
    r2 = find(b)

    if r1 != r2:
        parent[r2] = r1
        rank[r1] += rank[r2]


def find(a):
    if a == parent[a]:
        return a
    else:
        root = find(parent[a])
        parent[a] = root

        return parent[a]


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        F = int(input())
        parent = dict()
        rank = dict()

        for f in range(F):
            a, b = map(str, input().split(' '))
            if a not in parent:
                parent[a] = a
                rank[a] = 1

            if b not in parent:
                parent[b] = b
                rank[b] = 1

            union(a, b)
            print(rank[find(a)])





