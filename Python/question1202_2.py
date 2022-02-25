#보석 도둑
import heapq

if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    mass_and_val = list()

    for n in range(N):
        mass, val = map(int, input().split(' '))
        heapq.heappush(mass_and_val, (-val, val, mass))

    bag_capabilities = list()

    for k in range(K):
        heapq.heappush(bag_capabilities, int(input()))

    result = 0

    while mass_and_val:
        # 가방 용량 중에서, 보석을 수용할 수 있는 가장 작은 용량의 가방을 찾는다. -> 이분탐색
        priority, cur_val, cur_mass = heapq.heappop(mass_and_val)
        start = 0
        end = len(bag_capabilities)-1

        bound = -1

        while start <= end:
            mid = (start + end) //2
            if bag_capabilities[mid] >= cur_mass:
                end = mid - 1
                bound = mid

            else:
                start = mid + 1

        if bound != -1:
            bag_capabilities.pop(bound)
            result += cur_val

    print(result)

