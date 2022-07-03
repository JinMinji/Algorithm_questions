#등수 찾기, 골드 3
import sys

if __name__ == "__main__":
    N, M, X = map(int, sys.stdin.readline().split())

    rank_info = [[[],[]] for i in range(N+1)]

    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        rank_info[A][0].append(B)   # [0]작은쪽
        rank_info[B][1].append(A)   # [1]큰쪽

    visited = [[0, 0] for i in range(N+1)]
    to_visit = [[X, 0], [X, 1]]

    while to_visit:
        cur, d = to_visit.pop(0)
        if d == 0:  #작은쪽 탐색.
            for small_n in rank_info[cur][0]:
                if visited[small_n][0] == 0:
                    visited[small_n][0] = 1
                    to_visit.append([small_n, 0])
        else:
            for big_n in rank_info[cur][1]:
                if visited[big_n][1] == 0:
                    visited[big_n][1] = 1
                    to_visit.append([big_n, 1])

    left = 0
    right = 0
    for i in range(N+1):
        left += visited[i][0]
        right += visited[i][1]
    # print(visited)
    print(1+right, N-left)