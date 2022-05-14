#통학버스, 골드3

if __name__ == "__main__":
    N, K, S = map(int, input().split())

    left_list = list()
    right_list = list()

    for i in range(N):
        apt, num = map(int, input().split())
        distance = apt - S
        if distance <= 0:
            left_list.append([distance, num])

        else:
            right_list.append([distance, num])

    left_list.sort()
    right_list.sort()
    #
    # print(left_list)
    # print(right_list)

    bus = K     # 처음 출발 때 거리 값을 더해주려고 K(정원)로 시작.
    result = 0

    while left_list:
        # print(result)
        dis, num = left_list.pop(0)     #작은거부터
        bus += num
        # print(bus)
        while bus > K:
            bus -= K
            result += (-dis)*2     #왕복

    bus = K     # 처음 출발 때 거리 값을 더해주려고 K(정원)로 시작.

    for i in range(len(right_list)):
        # print(result)
        dis, num = right_list.pop()     #큰거부터
        bus += num
        # print(bus)
        while bus > K:
            bus -= K
            result += dis * 2  # 왕복

    print(result)