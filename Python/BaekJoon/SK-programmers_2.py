def solution(periods, payments, estimates):
    answer = [0, 0]
    for i in range(len(periods)):
        tmp_sum = sum(payments[i])

        if periods[i] < 23:  # 가입기간이 23개월 미만이면 이번달에도, 다음달에도 VIP가 될 수 없음.
            continue
        if periods[i] == 23:  # 가입기간이 23개월이면 이번달은 불가, 다음달은 90만 조건체크
            if tmp_sum - payments[i][0] + estimates[i] >= 900000:
                answer[0] += 1  # Not VIP -> VIP

        elif periods[i] < 59:  # 가입기간이 59개월 미만이면 90만 조건 체크.
            if tmp_sum >= 900000 and tmp_sum - payments[i][0] + estimates[i] < 900000:
                answer[1] += 1  # VIP -> Not VIP
            elif tmp_sum < 900000 and tmp_sum - payments[i][0] + estimates[i] >= 900000:
                answer[0] += 1  # Not VIP -> VIP

        elif periods[i] == 59:  # 가입기간이 59개월이면 이번달은 90만, 다음달은 60만 조건체크
            if tmp_sum >= 900000 and tmp_sum - payments[i][0] + estimates[i] < 600000:
                answer[1] += 1  # VIP -> Not VIP
            elif tmp_sum < 900000 and tmp_sum - payments[i][0] + estimates[i] >= 600000:
                answer[0] += 1  # Not VIP -> VIP

        else:  # 가입기간이 60개월이상이면 60만 조건체크
            if tmp_sum >= 600000 and tmp_sum - payments[i][0] + estimates[i] < 600000:
                answer[1] += 1  # VIP -> Not VIP
            elif tmp_sum < 600000 and tmp_sum - payments[i][0] + estimates[i] >= 600000:
                answer[0] += 1  # Not VIP -> VIP

    return answer


if __name__ == "__main__":
    print(solution([20, 23, 24], [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000]))
    print(solution([24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000]))