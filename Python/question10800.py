#컬러볼, 골드 3 맞았습니다


if __name__ == '__main__':
    N = int(input())
    balls = list()
    sizes = list()
    colors = [[] for i in range(N+1)]

    for i in range(N):
        c, s = map(int, input().split())
        balls.append([s, c, i])

    balls.sort(key=lambda x: (x[0], x[1]))

    result = [0 for i in range(N)]

    cur_total = 0
    colors_total = [[0, 0, 0] for i in range(N+1)]
    pre = 0
    same_total = 0
    for _ in range(len(balls)):
        s, c, i = balls[_]
        if pre == s:
            same_total += s
        else:
            same_total = 0

        if colors_total[c][0] == s:
            colors_total[c][1] += s
        else:
            colors_total[c][0] = s
            colors_total[c][1] = 0

        result[i] = cur_total - colors_total[c][2] - same_total + colors_total[c][1]
        colors_total[c][0] = s

        pre = s
        colors_total[c][2]+= s
        cur_total += s

    for i in range(N):
        print(result[i])

