# 컬러볼, 골드 3


if __name__ == '__main__':
    N = int(input())
    balls = list()
    sizes = list()
    colors = [[] for i in range(N + 1)]

    for i in range(N):
        c, s = map(int, input().split())
        balls.append([c, s])
        sizes.append(s)
        colors[c].append(s)

    sizes.sort()

    size_dp = list()
    size_dp.append(0)
    for i in range(1, sizes[-1]+1):
        if i in sizes:
            size_dp.append(size_dp[i - 1] + i*(sizes.count(i)))

        else:
            size_dp.append(size_dp[i-1])

    color_dp = list()
    for i in range(len(colors)):
        tmp_dp = list()
        if colors[i]:
            colors[i].sort()
            tmp_dp.append(0)
            for j in range(1, colors[i][-1]+1):
                if j in colors[i]:
                    tmp_dp.append(tmp_dp[j - 1] + j*(colors[i].count(j)))

                else:
                    tmp_dp.append(tmp_dp[j-1])

        color_dp.append(tmp_dp)

    for i in range(len(balls)):
        c, s = balls[i]
        print(size_dp[s] - color_dp[c][s])



