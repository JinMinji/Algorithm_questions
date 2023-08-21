
def solution(play_time, adv_time, logs):
    play_log = [0]*36000
    for i in logs:
        logtimes = list(i.split('-'))
        start = logtimes[0].split(':')
        end = logtimes[1].split(':')

        log_start = int(start[0])*360 + int(start[1])*60 + int(start[2])
        log_end = int(end[0]) * 360 + int(end[1]) * 60 + int(end[2])

        for i in range(log_start, log_end+1):
            play_log[i] += 1

    advlst = adv_time.split(":")
    avd = int(advlst[0]) * 360 + int(advlst[1]) * 60 + int(advlst[2])



    answer = ''
    return answer

solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
