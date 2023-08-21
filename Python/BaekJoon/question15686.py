#20210521 치킨배달
import itertools

def chicken_delivery(city_map):
    chicken = list()
    house = list()
    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 2: #치킨집 좌표만 따로 담기.
                chicken.append([i,j])
            elif city_map[i][j] == 1: #치킨집 좌표만 따로 담기.
                house.append([i,j])
    chicken_nCr = itertools.combinations(chicken, M)

    result = 10000000
    for picked_chicken in chicken_nCr:
        dist = list()
        for h in house:
            min_dist = 10000000
            for c in picked_chicken:
                min_dist = min(min_dist, (abs(h[0]-c[0])+abs(h[1]-c[1])))
            dist.append(min_dist)

        tmp_dist = 0
        for d in dist:
            tmp_dist += d

        result = min(result, tmp_dist)

    return result

def can_go(x, y):
    return 0 <= x < N and 0 <= y < 0

if __name__ == '__main__':
    N, M = map(int, input().split(" "))

    city_map = list()
    for _ in range(N):
        city_map.append(list(map(int, input().split(" "))))

    print(chicken_delivery(city_map))