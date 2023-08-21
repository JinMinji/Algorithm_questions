def solution(n):
    answer = -1
    # 1~9 -> 9 개 * 1
    # 10~99 -> 90 * 2
    # 100~999 -> 900 * 3
    # 1000~9999 -> 9000 * 4
    # 10000~99999 -> 90000 * 5
    # 100000~999999 -> 900000 * 6
    # max는 1_000_000_000 이므로!
    cnt = 0
    while True:
        # print(n, 9*(10**cnt))
        if n - (9*(10**cnt)*(cnt+1)) < 0:
            break
        n -= 9*(10**cnt)*(cnt+1)
        cnt += 1
    start = (10**cnt) - 1
    add_num = int(n // (cnt+1))
    remain = int(n % (cnt+1))

    # print(n, cnt, start, add_num, remain)

    if remain == 0:
        print(str(start + add_num), "마지막")
        answer = int(str(start + add_num)[-1])
    else:
        # print(str(start + add_num + 1), remain, "번째")
        answer = int(str(start + add_num + 1)[remain-1])

    return answer
