def solution(arr, processes):
    answer = []
    time = 0  # 최종 경과 시간
    read_standby = []  # 읽기 대기열
    write_standby = []  # 쓰기 대기열
    flag = 0  # 현재 종료상태(0)인지, 읽기상태(1)인지, 쓰기(2)상태인지
    cur_time = 1  # 현재 시간

    for p in range(len(processes)):  # 입력값 리스트로 변환
        tmp_list = list(processes[p].split(' '))
        if tmp_list[0] == 'read':  # 읽기
            processes[p] = [1, int(tmp_list[1]), int(tmp_list[2]), int(tmp_list[3]), int(tmp_list[4])]
        else:  # 쓰기
            processes[p] = [2, int(tmp_list[1]), int(tmp_list[2]), int(tmp_list[3]), int(tmp_list[4]), tmp_list[5]]

    while cur_time <= 100000:
        # 현재시간이 증가함에 따라, 대기열에 작업 추가
        while processes:
            if processes[0][1] <= cur_time:
                if processes[0][0] == 1:
                    read_standby.append(processes.pop(0))
                else:
                    write_standby.append(processes.pop(0))
            else:
                break

        if flag == 0:  # 종료 상태. 어떤 작업이든 가능
            if write_standby:  # 쓰기 작업이 먼저 수행되므로, 쓰기 대기열 먼저 확인
                flag = 2

            elif read_standby:  # 읽기 작업만 있으면, 읽기작업 수행
                flag = 1

            else:  # 대기열도 비어있고
                if not processes:  # 남은 작업도 없으면 종료
                    break

        if flag == 1:  # 읽기 상태, 읽기 작업은 동시에 가능
            max_time = 0
            tmp_add = 0
            can_go = True

            while can_go:
                while read_standby:  # 현재 읽기 대기열에 있는 읽기 작업들 전부 수행.
                    # - 읽기 작업 수행
                    tmp_list = read_standby.pop(0)
                    tmp_str = ''
                    for a in range(tmp_list[3], tmp_list[4] + 1):
                        tmp_str += arr[a]
                    print(tmp_str)
                    answer.append(tmp_str)
                    max_time = max(max_time, tmp_list[2] + tmp_add)  # 마지막 종료시간을 알기 위해, max값 저장.
                    # - 읽기 작업 수행

                tmp_add += 1  # 시간 1증가.
                tmp_len = len(processes)
                cnt = 0
                while processes and cnt <= tmp_len:
                    cnt += 1
                    # 대기열에 들어오지 않은 작업들 확인.
                    if processes[0][1] <= cur_time + tmp_add:
                        if processes[0][0] == 1:  # read작업의 경우 대기열에 넣어주고,
                            read_standby.append(processes.pop(0))
                        else:  # write 작업이 대기할 경우에는 쓰기 작업을 먼저해야함.
                            write_standby.append(processes.pop(0))
                            can_go = False
                            break

                if not read_standby:
                    can_go = False

            time += max_time
            cur_time += max_time
            flag = 0

        elif flag == 2:  # 쓰기 상태, 모든 작업 대기열로.
            if write_standby:
                # 쓰기 작업 수행 -
                tmp_list = write_standby.pop(0)
                time += tmp_list[2]  # 소요시간
                for a in range(tmp_list[3], tmp_list[4] + 1):
                    arr[a] = tmp_list[5]
                print(arr)
                cur_time += tmp_list[2]
                # - 쓰기 작업 수행

            flag = 0

        cur_time += 1

    answer.append(time)

    return answer


if __name__ == '__main__':
    # arr = ["1","2","4","3","3","4","1","5"]
    # processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
    # print(solution(arr, processes))

    arr = ["1","1","1","1","1","1","1"]
    processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
    print()
    print(solution(arr, processes))