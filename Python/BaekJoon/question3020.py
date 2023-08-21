# 20210601 개똥벌레

def find_min(h):
    up_num = lower_bound(h, cave_up)
    down_num = lower_bound(H-h-1, cave_down)
    return up_num + down_num

def lower_bound(h, height_list):
    start = 0
    end = len(height_list)-1
    while start <= end:
        mid = (start + end) // 2
        if height_list[mid] <= h:
            start = mid+1
        else:
            end = mid-1
    return len(height_list[end+1:])

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



