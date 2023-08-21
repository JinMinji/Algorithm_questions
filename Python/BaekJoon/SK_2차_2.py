import heapq


def push_standby(process):
    global standby

    tmp_list = list(process.split(' '))
    if tmp_list[0] == 'read':
        heapq.heappush(standby, [int(tmp_list[1]), 1, int(tmp_list[2]), int(tmp_list[3]), int(tmp_list[4])])

    else:
        heapq.heappush(standby, [int(tmp_list[1]), 0, int(tmp_list[2]), int(tmp_list[3]), int(tmp_list[4]), tmp_list[5]])


def solution(arr, processes):
    answer = []
    time = 0  # 최종 경과 시간
    global standby
    standby = []  # 대기열

    cur_time = int(list(processes[0].split(' '))[1])
    push_standby(processes.pop(0))
    # 같은 시간에 요청되는 작업은 없으므로, 첫번째부터 작업요청은 바로 시작.

    while standby or processes:
        if standby:
            tmp_list = heapq.heappop(standby)
            if tmp_list[1] == 1:
                print('read')
                time += tmp_list[2]  # 소요시간
                tmp_str = ''
                for a in range(tmp_list[3], tmp_list[4] + 1):
                    tmp_str += arr[a]
                answer.append(tmp_str)
                cur_time += tmp_list[2]

            else:  # tmp_list == 'write':
                print('write')
                time += tmp_list[2]  # 소요시간
                for a in range(tmp_list[3], tmp_list[4] + 1):
                    arr[a] = tmp_list[5]

                cur_time += tmp_list[2]
        else:
            cur_time += 1

        print('대기열 :', standby)
        print('answer :', answer)
        # print(processes)

        while processes:
            tmp = list(processes[0].split(' '))
            if int(tmp[1]) <= cur_time:
                push_standby(processes.pop(0))
            else:
                break
        print()

    answer.append(time)

    return answer


if __name__ == '__main__':
    arr = ["1","2","4","3","3","4","1","5"]
    processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
    print(solution(arr, processes))