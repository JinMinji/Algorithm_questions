def solution(money, costs):
    answer = 0

    # [1, 5, 10, 50, 100, 500]
    # *5, *2, *5, *2, *5

    tmp_l = [1, 5, 10, 50, 100, 500]

    for i in range(len(costs)-1):
        costs[i+1] = min(costs[i] * (tmp_l[i+1]//tmp_l[i]), costs[i+1])

    for k in range(1, len(tmp_l)+1):
        cur_cnt = money // tmp_l[-k]
        money = money - (tmp_l[-k] * cur_cnt)
        answer += costs[-k] * cur_cnt

    return answer


if __name__ == '__main__':
    print(solution(4578, [1, 4, 99, 35, 50, 1000]))