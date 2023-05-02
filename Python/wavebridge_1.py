def solution(n, m, x_axis, y_axis):
    answer = 0
    # 어차피 일자로 쭉 다 잘리니까, X max gap * Y max gap 하면 됨
    x_axis.append(n)
    y_axis.append(m)
    pre = 0
    x_max = 0

    for x in x_axis:
        x_max = max(x_max, x - pre)
        pre = x

    pre = 0
    y_max = 0
    for y in y_axis:
        y_max = max(y_max, y - pre)
        pre = y

    answer = x_max * y_max

    return answer