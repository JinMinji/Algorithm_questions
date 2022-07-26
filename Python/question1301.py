# 1310, 비즈공예, 골드4
import sys
from functools import reduce

if __name__ == "__main__":
    N = int(input())
    marbles = [0 for i in range(N)]
    for i in range(N):
        marbles[i] = int(input())

    # 123 132 213 231 312 321
    # 3~5종, 10개이하.
    M = sum(marbles)
    # C = reduce(lambda x, cur: x*(cur+1), marbles, 1)
    C = 11**N

    dp = [M][]
    # 3차원 배열

    for i in range(N):
        dp[0][] = 1
        # 0개 까지 뀄을 때
        # i번째 구슬이 앞에 1개 있고,
        # 남은 구슬의 개수

    # for i in range(1, M):
    #     for j in range(N*3):
    #         m_i = j // 3
    #         m_cnt = j % 3
    #         # m
    #         for k in range(11):
    #             dp[i][j][k] = dp[i-1][m_i*3][k]
    #             dp[i][j][k] = dp[]
    #
    #         if m_cnt == 2:  # 앞서 두개를 이미 놨으면, 3개는 못놓는다!