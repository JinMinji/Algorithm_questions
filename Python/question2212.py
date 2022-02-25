# 센서

def solutions(sensor_list, k):
    distance_list = list()

    # 좌표값의 최소 : 0 혹은 sensor_list[0]
    # 좌표값의 최대 : 1000000 혹은 sensor_list[-1]
    for i in range(1, len(sensor_list)):
        distance_list.append(sensor_list[i] - sensor_list[i-1])

    distance_list.sort()

    return sum(distance_list[:len(sensor_list) - k])


if __name__ == '__main__':
    N = int(input())    # 센서의 개수, 1 <= N <= 10000
    K = int(input())    # 집중국의 개수, 1 <= K <= 1000
    sensors = list(map(int, input().split(' ')))    # 센서의 좌표

    sensors.sort()  # 순서대로 정렬

    if N == 1:
        print(0)
    else:
        print(solutions(sensors, K))


