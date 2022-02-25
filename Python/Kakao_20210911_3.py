# 주차요금
import math

def cal_time(in_time, out_time):
    if out_time == '':
        out_time = '23:59'

    in_times = in_time.split(':')
    out_times = out_time.split(':')

    hour = int(out_times[0]) - int(in_times[0])
    minute = int(out_times[1]) - int(in_times[1])

    if minute < 0:
        hour -= 1
        minute += 60

    total_time = hour * 60 + minute

    return total_time


def solution(fees, records):
    answer = []
    cars = dict()
    for i in range(len(records)):
        time, car, in_out = records[i].split(' ')

        cars[car] = cars.get(car, [0, ''])       # time, last time

        if cars[car][1] == '':  # IN이라는 뜻,
            cars[car][1] = time

        else:   # OUT이라는 뜻
            total_time = cal_time(cars[car][1], time)
            cars[car][0] += total_time
            cars[car][1] = ''

    for key, value in cars.items():
        if value[1] != '':
            total_time = cal_time(value[1], '23:59')
            cars[key][0] += total_time
            cars[key][1] = ''

        if cars[key][0] <= fees[0]:
            answer.append([int(key), fees[1]])

        else:
            extra = math.ceil((cars[key][0] - fees[0]) / fees[2]) * fees[3]
            answer.append([int(key), fees[1]+extra])


    answer.sort(key=lambda x:x[0])

    for i in range(len(answer)):
        answer[i] = answer[i][1]

    return answer


if __name__ == '__main__':
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))