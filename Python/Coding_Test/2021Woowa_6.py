def time_to_int(a):
    time = int(a[:-2])  # 최소단위 1시간이므로 분은 신경쓸 필요 없음
    if a[-2:] == 'AM':
        return time
    else:  # PM
        return time + 12


def solution(time, plans):  # 첫번째 여행지도 못가면??? 그러면 마지막여행지는 무엇을 리턴해야하는가
    answer = ''
    for i in range(len(plans)):
        loc, d_time, a_time = plans[i]
        # 월요일 출근시간 : 1PM => 13      #MAX근무시간 : 5
        # 금요일 퇴근시간 : 6PM => 18      #MAX근무시간 : 8.5
        d_time = time_to_int(d_time)
        a_time = time_to_int(a_time)

        tmp_d, tmp_a = 0, 0
        if d_time < 18:
            tmp_d = min(18- d_time, 8.5)

        if a_time > 13:
            tmp_a = min(a_time - 13, 5)

        if time >= tmp_d + tmp_a:
            answer = loc
            time -= tmp_d + tmp_a

    return answer


if __name__ == '__main__':
    print(solution(3.5, [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]))