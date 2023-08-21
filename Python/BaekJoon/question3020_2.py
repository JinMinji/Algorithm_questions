# 20210601 개똥벌레
import bisect
import sys
input = sys.stdin.readline

def find_min(h):
    up_num = len(cave_up) - bisect.bisect_right(cave_up, h)
    down_num = len(cave_down) - bisect.bisect_right(cave_down, H-h-1)
    return up_num + down_num

if __name__ == '__main__':
    N, H = map(int, input().split(" "))

    cave_up = list()    #석순
    cave_down = list()   #종유석

    for i in range(N):
        if i % 2 == 0:
            cave_up.append(int(input()))
        else:
            cave_down.append(int(input()))

    cave_up.sort()
    cave_down.sort()

    result = N
    cnt = 0

    for i in range(H):
        tmp = find_min(i)
        if tmp < result:
            result = tmp
            cnt = 1
        elif tmp == result:
            cnt += 1

    print(result, cnt)



