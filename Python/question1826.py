#연료채우기, 골드3
#슬라이싱은 효율이 최악


if __name__ == "__main__":
    N = int(input())
    gas_station = [0 for i in range(10**6+1)]
    # 성경이의 시작위치를 0이라고 두고, 거리의 max는 10**6이므로
    # 10**6 만큼의 배열을 만들고, 주유소가 있는 위치에 주유 가능한 기름 값을 넣는다.
    for i in range(N):
        idx, oil = map(int, input().split())
        if gas_station[idx] != 0:   # 같은 위치에 두개가 있으면?? -> 둘 중하나만? 둘 다?
            gas_station[idx] = max(gas_station[idx], oil)

        else:
            gas_station[idx] = oil

    distance, cur_oil = map(int, input().split())

    answer = 0
    cur_loc = 0
    while cur_loc + cur_oil < distance:     #현재 위치 + 가진 오일이 목적지를 넘기 전까지만 확인
        tmp_end = min(cur_loc + cur_oil + 1, 10**6)     #일단 현재까지 갈 수 있는 위치 + 1 (슬라이스 할거라서 1 더해줌)
        if sum(gas_station[cur_loc + 1:tmp_end]) == 0:
            #아예 빠져나가지 못하는 경우도 check!
            answer = -1
            break
        cur_max = max(gas_station[cur_loc+1:tmp_end])   #cur_loc은 이미 주유한 곳이니까, 무시하고 +1 위치부터
        max_idx = gas_station[cur_loc+1:tmp_end].index(cur_max) + cur_loc + 1   # 다음 맥스주유소 위치
        cur_oil -= max_idx - cur_loc        # 현위치~맥스주유소 위치 까지 이동한 기름은 빼주고
        cur_loc = max_idx       # 현위치는 맥스주유소 위치로 변경
        cur_oil += cur_max      # 기름에 맥스주유소에서 얻은 기름 더해준다.
        answer += 1             # 주유소 들렀으니까 +1
        # print("현재 위치 :", cur_loc)
        # print("현재 연료 :", cur_oil)
        # print()



    print(answer)

