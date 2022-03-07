#보석 도둑


if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    mass_and_val = list()

    for n in range(N):
        mass, val = map(int, input().split(' '))
        heapq.heappush(mass_and_val, (-val, val, mass))

    bag_capabilities = list()

    for k in range(K):
        heapq.heappush(bag_capabilities, int(input()))



