# 오름세, 골드 2


def solutions(N):
    arr = list(map(int, input().split(' ')))    # 주가 입력

    tmp_arr = list()    # 오름세 길이를 담을 배열

    tmp_arr.append(arr[0])

    for i in range(1, len(arr)):
        s = 0
        e = len(tmp_arr) - 1
        idx = 0
        while s <= e:
            mid = (s+e)//2

            if tmp_arr[mid] < arr[i]:
                idx = mid
                s = mid + 1

            else:
                e = mid - 1

        if idx == len(tmp_arr) - 1:
            tmp_arr.append(arr[idx])

        else:
            tmp_arr[idx] = arr[idx]

        return len(tmp_arr)


if __name__ == '__main__':
    while True:
        N = input()
        if not N:
            break
        N = int(N)
        dp = list()
        print(solutions(N))