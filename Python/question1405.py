# 미친 로봇 골드 5
dx = [0, 0, 1, -1]
dy = [-1, 1,  0, 0]


def go(visited, i, j, cur_prob):
    global result, prob, N

    if len(visited) == N + 1:
        result += cur_prob
        return

    for _ in range(4):
        x = i + dx[_]
        y = j + dy[_]
        if [x, y] not in visited:
            visited.append([x, y])
            go(visited, x, y, cur_prob*prob[_])
            visited.pop()


if __name__ == '__main__':
    N, e, w, s, n = map(int, input().split(' '))

    prob = [e, w, s, n]

    visited = list()
    result = 0.0

    visited.append([0, 0])
    go(visited, 0, 0, 1)

    print(result * 0.01 **N)


