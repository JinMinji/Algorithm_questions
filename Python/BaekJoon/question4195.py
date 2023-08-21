# 어렵따...!!!!!!!!!!!
# 다시 풀어보기 - 풀이 (유형별 문제풀이 - 3. 고급자료구조)

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

casenum = int(input())

for i in range(casenum):
    parent = {}
    number = {}

    F = int(input())
    for j in range(F):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a,b)

        print(number[find(a)])


        parent[b] = a



