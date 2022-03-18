# 가운데를 말해요 골드 2


def lower_bounds(num):
    global num_list
    idx = -1

    start = 0
    end = len(num_list) - 1

    if num_list[start] > num:
        num_list.insert(0, num)
        return

    elif num_list[end] < num:
        num_list.append(num)
        return

    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] < num:
            idx = mid
            start = mid + 1

        else:
            end = mid - 1

    num_list.insert(idx+1, num)


if __name__ == '__main__':
    N = int(input())

    num_list = [int(input())]
    print(num_list[0])

    for i in range(N-1):
        n = int(input())
        lower_bounds(n)
        # print(num_list, (i+1) // 2)
        print(num_list[(i+1) // 2])
