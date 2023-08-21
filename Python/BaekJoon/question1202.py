#보석 도둑

if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    mass_and_val = list()

    for n in range(N):
        mass_and_val.append(list(map(int, input().split(' '))))

    bag_capabilities = list()

    for k in range(K):
        bag_capabilities.append(int(input()))

    mass_and_val.sort(key=lambda x: x[1], reverse=True)   # 가격 큰 순서로 정렬
    bag_capabilities.sort()     # 용량 큰 순서로 정렬

    result = 0

    for i in range(len(mass_and_val)):
        # 가방 용량 중에서, 보석을 수용할 수 있는 가장 작은 용량의 가방을 찾는다. -> 이분탐색
        start = 0
        end = len(bag_capabilities)-1

        bound = -1

        while start <= end:
            mid = (start + end) //2
            if bag_capabilities[mid] >= mass_and_val[i][0]:
                end = mid - 1
                bound = mid

            else:
                start = mid + 1

        if bound != -1:
            bag_capabilities.pop(bound)
            result += mass_and_val[i][1]

    print(result)

