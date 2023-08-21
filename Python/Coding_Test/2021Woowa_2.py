def to_time(a):
    atime = a.split(':')
    atime = int(atime[0]) * 60 + int(atime[1])

    return atime


def solution(log):
    total = 0

    for i in range(len(log) // 2):
        tmp_time = to_time(log[2*i + 1]) - to_time(log[2*i])
        if tmp_time < 5:
            tmp_time = 0
        elif tmp_time > 105:  # 1시간 45분
            tmp_time = 105
        total += tmp_time

    hours = total // 60
    minutes = total % 60

    answer = str(hours).zfill(2) + ':' + str(minutes).zfill(2)

    return answer


if __name__ == '__main__':
    print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
    print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))