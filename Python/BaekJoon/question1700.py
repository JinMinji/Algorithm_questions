#멀티탭 스케줄링

if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    appliances = list(map(int, input().split(' ')))

    multitap = [0 for i in range(N)]

    cnt_result = 0

    for i in range(K):
        # print(multitap)
        if appliances[i] in multitap:
            # print(appliances[i], 'in')
            continue

        if N == 1:
            # print(appliances[i], 'in')
            cnt_result += 1
            continue

        if 0 in multitap:
            # print(appliances[i], 'in')
            for m in range(N):
                if multitap[m] == 0:
                    multitap[m] = appliances[i]
                    break

        else:
            tmp_tap = [1 for i in range(N)]
            differ_cnt = 0
            if K-i == 1:
                cnt_result += 1
                continue
            for _ in range(i+1, K):
                if appliances[_] not in multitap:
                    differ_cnt += 1
                    if differ_cnt >= N:
                        # print(multitap[0], 'out')
                        # print(appliances[i], 'in')
                        multitap[0] = appliances[i]
                        cnt_result += 1
                        break
                else:
                    tmp_tap[multitap.index(appliances[_])] = 0
                    if sum(tmp_tap) == 1:
                        # print(multitap[tmp_tap.index(1)], 'out')
                        # print(appliances[i], 'in')
                        multitap[tmp_tap.index(1)] = appliances[i]
                        cnt_result += 1
                        break


    print(cnt_result)