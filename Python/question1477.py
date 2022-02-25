#20210804 휴게소 세우기
N, M, L = 0, 0, 0


def ispossible(loc, dist):
    rest = M
    pre = 0
    for p in loc:
        while(p - pre) > dist:
            if rest > 0:
                rest -= 1
                pre += dist
            else:
                return False
        pre = p

    if (pre + dist) < L:
        while (pre + dist) < L:
            if rest > 0:
                rest -= 1
                pre += dist
            else:
                return False
    return True


def find_min_dist(loc):
    result = L      # max

    start = 0
    end = L
    while start < end:
        mid = (start+end)//2
        if ispossible(loc, mid):
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    return result


if __name__ == '__main__':
    N, M, L = map(int, input().split())
    locations = list(map(int, input().split()))

    locations.sort()    #순서대로 정렬하기

    print(find_min_dist(locations))