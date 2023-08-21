#20210727 나의 인생에는 수학과 함께
# 전역변수로 선언
min_dp = list()
max_dp = list()
max_val = 50000


def change_cal(x1, x2, operator):
    a = int(x1)
    b = int(x2)
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:  #'/'
        return a / b


def min_res(graph, x, y):   # 인덱스의합이 짝수인것이 숫자, 홀수인것이

    if min_dp[x][y] != max_val:    # 이미 구해둔 값이 있으면,
        return min_dp[x][y]

    # 위에서 내려왔거나, [x][y-1]
    # 왼쪽에서 오른쪽으로 온 경우! [x-1][y]
    # A + B
    # - C *
    # D / E
    # 의 경우, E로 가는 방법은, 위 '*'와 좌 '/'이고
    # '*'로 가는 방법은, B나 C,
    # '/'로 가는 방법은, C나 D 이므로 비교해줘야하는 값은
    # 'dp[D] / E' vs 'dp[C] / E' vs 'dp[B] * E' vs 'dp[C] * E'
    # 위 4가지다.

    tmp_min = max_val

    if 0 <= x-1:   # 위쪽
        tmp_operator = graph[x-1][y]
        if 0 <= x - 2:  # 위쪽
            tmp_min = min(tmp_min, change_cal(min_res(graph, x-2, y), graph[x][y], tmp_operator))

        if 0 <= y - 1:  # 왼쪽
            tmp_min = min(tmp_min, change_cal(min_res(graph, x-1, y-1), graph[x][y], tmp_operator))

    if 0 <= y-1:   # 왼쪽
        tmp_operator = graph[x][y-1]
        if 0 <= x-1:    # 위쪽
            tmp_min = min(tmp_min, change_cal(min_res(graph, x-1, y-1), graph[x][y], tmp_operator))

        if 0 <= y-2:    # 왼쪽
            tmp_min = min(tmp_min, change_cal(min_res(graph, x, y - 2), graph[x][y], tmp_operator))

    min_dp[x][y] = tmp_min

    return min_dp[x][y]


def max_res(graph, x, y):

    if max_dp[x][y] != -max_val:    # 이미 구해둔 값이 있으면,
        return max_dp[x][y]

    tmp_max = -max_val

    if 0 <= x - 1:  # 위쪽
        tmp_operator = graph[x - 1][y]
        if 0 <= x - 2:  # 위쪽
            tmp_max = max(tmp_max, change_cal(max_res(graph, x - 2, y), graph[x][y], tmp_operator))

        if 0 <= y - 1:  # 왼쪽
            tmp_max = max(tmp_max, change_cal(max_res(graph, x - 1, y - 1), graph[x][y], tmp_operator))

    if 0 <= y - 1:  # 왼쪽
        tmp_operator = graph[x][y - 1]
        if 0 <= x - 1:  # 위쪽
            tmp_max = max(tmp_max, change_cal(max_res(graph, x - 1, y - 1), graph[x][y], tmp_operator))

        if 0 <= y - 2:  # 왼쪽
            tmp_max = max(tmp_max, change_cal(max_res(graph, x, y - 2), graph[x][y], tmp_operator))

    max_dp[x][y] = tmp_max

    return max_dp[x][y]


if __name__ == '__main__':
    N = int(input())

    map_list = list()
    for i in range(N):
        map_list.append(list(map(str, input().split())))

    min_dp = [[max_val for i in range(N)] for i in range(N)]
    max_dp = [[-max_val for i in range(N)] for i in range(N)]
    start = [0, 0]
    end = [N-1, N-1]
    now_min = max_val
    now_max = 0
    now_x, now_y = 0, 0
    min_dp[0][0], max_dp[0][0] = map_list[0][0], map_list[0][0]
    print(max_res(map_list, N-1, N-1), min_res(map_list, N-1, N-1))
