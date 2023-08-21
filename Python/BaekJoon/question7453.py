#합이 0인 네 정수, 골드 2
import sys

# AB, CD 묶어서 풀어야한다.
#는 거는 어케 알았어여 원대님?

if __name__ == '__main__':
    N = int(input())

    alpha_set = [[] for i in range(4)]
    AB = dict()

    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))

        for k in range(4):
            alpha_set[k].append(tmp[k])

    for i in range(N):
        for j in range(N):
            AB[alpha_set[0][i] + alpha_set[1][j]] = AB.get(alpha_set[0][i] + alpha_set[1][j], 0)
            AB[alpha_set[0][i] + alpha_set[1][j]] += 1

    result = 0
    for i in range(N):
        for j in range(N):
            result += AB.get(-(alpha_set[2][i] + alpha_set[3][j]), 0)

    print(result)