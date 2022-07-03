# SHOW ME THE DUNGEON
import sys


def m_total(m_lst):
    m_lst.sort()
    result = 0
    for i in range(len(m_lst)):
        result += m_lst[i]*len(m_lst)-i-1

    return result


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    monsters = list(map(int, sys.stdin.readline().split()))
    people = list(map(int, sys.stdin.readline().split()))

    dp = [[[0, []] for i in range(K + 1)] for i in range(N + 1)]

    for i in range(N + 1):
        for a in range(K + 1):

            if i == 0 or a == 0:
                continue

            if monsters[i-1] <= a:  # i번째 섬을 들를 수 있을 때
                if people[i-1] + dp[i-1][a - monsters[i-1]][0] > dp[i-1][a][0]:
                    dp[i][a][0] = dp[i-1][a - monsters[i-1]][0] + people[i-1]
                    dp[i][a][1] = dp[i-1][a - monsters[i-1]][1] + [monsters[i-1]]
                else:
                    dp[i][a] = dp[i-1][a]

            else:
                dp[i][a] = dp[i - 1][a]

    INF = float('inf')
    p_dp = [INF for i in range(sum(people)+1)]

    # for i in range(len(dp)):
    #     print(dp[i])

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            tmp = m_total(dp[i][j][1])
            # print(i, j, dp[i][j][1], tmp)
            if p_dp[dp[i][j][0]] > tmp:
                p_dp[dp[i][j][0]] = tmp

    start = 0
    end = sum(people)

    answer = 0
    while start <= end:
        # print(start, end)
        mid = (start + end) // 2

        if mid > dp[N][K][0]:
            end = mid - 1

        if min(p_dp[mid:]) <= K:
            # print("here", answer, mid)
            start = mid + 1
            answer = mid

        else:
            end = mid - 1

    # for i in range(len(dp)):
    #     print(dp[i])
    # print(p_dp)
    print(answer)