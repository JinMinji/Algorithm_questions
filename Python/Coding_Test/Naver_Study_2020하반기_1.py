# 탁구공 공장

def solutions(n, p, c):
    answer = 0
    cur_stock = 0
    cur_cnt = 0
    total = 0
    days = 0
    for i in range(n):
        days += 1
        cur_stock += p[i]
        if cur_stock >= c[i]:   #납품완료
            cur_stock -= c[i]
            total += c[i]*(100//(2**cur_cnt))
            cur_cnt = 0
        else:   #납품실패
            cur_cnt += 1
            if cur_cnt >= 3:
                break

    answer = (round(total / days, 2))

    return answer


if __name__ == '__main__':
    print(solutions(6, [5, 4, 7, 2, 0, 6], [4, 6, 4, 9, 2, 3]))
    print(solutions(7, [6, 2, 1, 0, 2, 4, 3], [3, 6, 6, 2, 3, 7, 6]))

    print('{:.2f}'.format(solutions(6, [5, 4, 7, 2, 0, 6], [4, 6, 4, 9, 2, 3])))
    print('{:.2f}'.format(solutions(7, [6, 2, 1, 0, 2, 4, 3], [3, 6, 6, 2, 3, 7, 6])))