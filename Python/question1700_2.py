#멀티탭 스케줄링

if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    appliances = list(map(int, input().split(' ')))

    multitap = [0 for i in range(N)]        # 멀티탭에 현재 꽂힌 전자기기

    cnt_result = 0

    for i in range(K):

        if appliances[i] in multitap:   # 이미 멀티탭에 꽂혀 있을 때
            continue

        if 0 in multitap:   # 안 꽂힌 빈자리가 있을 때
            for m in range(N):
                if multitap[m] == 0:
                    multitap[m] = appliances[i]
                    break

        else:   # 하나를 뽑고 꽂아야 할 때
            tmp_tap = [1 for i in range(N)]     # 현재 멀티탭에 꽂힌 기기가 이후 등장하는 지 체크

            change_tap = -1

            for _ in range(i+1, K):     # 이후를 체크하면서,
                if appliances[_] in multitap:
                    tmp_tap[multitap.index(appliances[_])] = 0  # 나오면 0으로 체크

                if sum(tmp_tap) == 1:   # 안나온게 1개면, 멀티탭에 꽂혀있는 기기 중 가장 나중에 나오는 것이 그 기기.
                    change_tap = tmp_tap.index(1)
                    multitap[change_tap] = appliances[i]
                    cnt_result += 1
                    break

            if change_tap == -1:
                if sum(tmp_tap) > 0:    # => 다 돌았지만, 안나온 게 1개 이상이다, 그럼 안나온 것 중에 아무거나 바꿔주면됨
                    change_tap = tmp_tap.index(1)
                else:
                    change_tap = 0

                multitap[change_tap] = appliances[i]
                cnt_result += 1


    print(cnt_result)