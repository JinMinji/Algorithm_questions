# 20210605 프로그래머스
# 광고삽입 Level

def solution(play_time, adv_time, logs):
    answer = ''
    # 100시간은 36만초
    # log의 max는 30만

    # 재생시간 초단위로 변환
    tmp_list = list(map(int, play_time.split(':')))
    p_time = tmp_list[0] * 3600 + tmp_list[1] * 60 + tmp_list[2]
    play_time_list = [0 for i in range(p_time + 1)]

    # 광고시간 초단위로 변환
    tmp_list = list(map(int, adv_time.split(':')))
    a_time = tmp_list[0] * 3600 + tmp_list[1] * 60 + tmp_list[2]

    # 사용자 시청기록
    for log in logs:
        start, end = log.split('-')

        tmp_list = list(map(int, start.split(':')))
        start_time = tmp_list[0] * 3600 + tmp_list[1] * 60 + tmp_list[2]

        tmp_list = list(map(int, end.split(':')))
        end_time = tmp_list[0] * 3600 + tmp_list[1] * 60 + tmp_list[2]

        # 시작시간부터, 종료시간까지 돌면서, count +1
        for i in range(start_time, end_time + 1):
            play_time_list[i] += 1

    # 구간합 담아줄 total_time
    total_time = 0
    # 처음 0초부터 시작!
    for i in range(a_time+1):
        total_time += play_time_list[i]

    answer_time = 0     # 0초부터 시작
    max_time = total_time   # max 합을 담아줄 변수
    answer_time = max_time

    for i in range(1, p_time - a_time + 1):     # 1초부터 ~ 전체시간-광고시간 까지!
        total_time -= play_time_list[i - 1]
        total_time += play_time_list[i + a_time]
        if total_time > max_time:
            answer_time = i
            max_time = total_time

    # 결과 다시 string으로 변환
    h = answer_time // 3600
    m = (answer_time % 3600) // 60
    s = (answer_time % 3600) % 60

    answer = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

    return answer

if __name__ == "__main__":
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    print(solution(play_time, adv_time, logs))