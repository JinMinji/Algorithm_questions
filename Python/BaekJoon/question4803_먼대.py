import sys
input = sys.stdin.readline


def find(n):
    if p[n] == n:
        return n

    p[n] = find(p[n])
    return p[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    p[b] = a


if __name__ == '__main__':
    test = 1

    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            break

        treeCnt = 0
        p = [i for i in range(N+1)]

        treeSet = set()
        noTreeSet = set()

        for _ in range(M):
            a, b = map(int, input().split())

            if find(a) != find(b):
                union(a, b)
            else:
                # union(a, b)
                noTreeSet.add(find(a))

        for i in range(1, N+1):
            treeSet.add(p[i])

        treeCnt = len(treeSet.difference(noTreeSet))

        if treeCnt > 1:
            print('Case %d: A forest of %d trees.' % (test, treeCnt))
        elif treeCnt == 1:
            print('Case %d: There is one tree.' % test)
        else:
            print('Case %d: No trees.' % test)

        test += 1