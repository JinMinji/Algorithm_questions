#SHOW ME THE DUNGEON
import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    monsters = list(map(int, sys.stdin.readline().split()))
    people = list(map(int, sys.stdin.readline().split()))

    # K만큼의 체력으로 N섬을 들렀을 때 최대로 구할 수 있는 사람 수
    dp = [[0 for i in range(K+1)] for i in range(N+1)]

    for i in range(N+1):
        for a in range(K+1):

            if i == 0 or a == 0:
                dp[i][a] = 0
                continue

            if monsters[i-1] <= a:    # i번째 섬을 들를 수 있을 때
                # i번째 섬까지 고려할 때
                # a의 체력으로 방문할 때 구할 수 있는 최대사람 수는
                # i번째 섬을 방문하지 않았을 때의 최대사람수
                # vs i번째섬을 방문하고, a-monster[i]의 체력으로 방문할 수 있는 최대 사람수의 합

                dp[i][a] = max(people[i-1] + dp[i-1][a-monsters[i-1]], dp[i-1][a])

            else:
                dp[i][a] = dp[i-1][a]

    # K의 체력으로 구할 수 있는 사람 수
    for i in range():
        print(dp[N][K])