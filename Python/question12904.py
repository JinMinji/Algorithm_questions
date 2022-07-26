#12904, A와 B, 골드5
import sys
from collections import deque

if __name__ == "__main__":
    S = list(sys.stdin.readline().rstrip('\n'))
    T = list(sys.stdin.readline().rstrip('\n'))

    # target -> start
    # A를 붙이는 작업, 뒤집고 B를 붙이는 작업. 둘 중에 어떤 게 더 이득인지 판단하는 방법??
    answer = 0
    cur = -1
    while len(T) >= len(S):
        # print(T, cur)
        if cur == -1 and T == S:
            answer = 1
            break
        elif cur == 0 and T == S[::-1]:
            answer = 1
            break

        if T[cur] == 'A':
            T.pop(cur)

        elif T[cur]:
            if cur == -1:
                T.pop(cur)
                cur = 0
            else:
                T.pop()
                cur = -1
        else:
            answer = 0
            break

    print(answer)

