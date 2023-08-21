#15900, 나무 탈출, 실버1
import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    tree = [[] for i in range(N)]

    for i in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    to_visit = deque()
    to_visit.append(0)  # 0번은 루트노드
    visited = [0 for i in range(N)]
    answer = 0
    while to_visit:
        cur = to_visit.popleft()
        for i in range(len(tree[cur])):
            if visited[tree[cur][i]] == 0:
                visited[tree[cur][i]] = visited[cur]+1
                to_visit.append(tree[cur][i])

            if len(tree[cur]) == 1 and cur != 0:
                answer += visited[cur]

    if answer % 2 == 0:
        print("No")
    else:
        print("Yes")