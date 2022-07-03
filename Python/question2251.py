#물통, 골드5
import sys


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())

    # 3개의 물통, 물통끼리 물을 옮기는 방법은
    # A -> B, A -> C
    # B -> A, B -> C
    # C -> A, C -> B
    # 총 6개.
    # 이 때, 시작 물통에 물이 없으면, 의미가 없음.

    to_visit = [[0, 0, C]]
    visited = [0 for i in range(C+1)]
    visited[C] = 1
    while to_visit:
        a, b, c = to_visit.pop(0)

        if a != 0:
            # B주기
            if B != b:
                if B-b >= a and [0, b+a, c] not in visited:
                    to_visit.append([0, b+a, c])
                elif B-b < a and [a-(B-b), B, c] not in visited:
                    to_visit.append([a-(B-b), B, c])

            # C주기
            if C != c:
                if C-c >= a and [0, b, c+a] not in visited:
                    to_visit.append([0, b, c+a])
                elif C-c < a and [a-(C-c), b, C] not in visited:
                    to_visit.append([a-(C-c), b, C])

        if b != 0:
            # A주기
            if A != a:
                if A - a >= b and [a+b, 0, c] not in visited:
                    to_visit.append([a+b, 0, c])
                elif A - a < b and [A, b-(A-a), c] not in visited:
                    to_visit.append([A, b-(A-a), c])

            # C주기
            if C != c:
                if C - c >= b and [a, 0, c + b] not in visited:
                    to_visit.append([a, 0, c + b])
                elif C - c < b and [a, b - (C - c), C] not in visited:
                    to_visit.append([a, b - (C - c), C])

        if c != 0:
            # A주기
            if A != a:
                if A - a >= c and [a + c, b, 0] not in visited:
                    to_visit.append([a + c, b, 0])
                elif A - a < c and [A, b, c - (A - a)] not in visited:
                    to_visit.append([A, b, c - (A - a)])

            # B주기
            if B != b:
                if B - b >= c and [a, b + c, 0] not in visited:
                    to_visit.append([a, b + c, 0])
                elif B - b < c and [a, B, c - (B - b)] not in visited:
                    to_visit.append([a, B, c - (B - b)])

    for i in range(len(visited)):
        if visited[i]:
            print(i, end=" ")





