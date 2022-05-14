#모자이크, 골드 3
# **밑변에 맞추어 붙임**
# -> 코드로는 맨위 행부터


def can_mosaic(size):
    global wrongs, sheets, row_max

    if size >= row_max: #행 최대 길이 체크
        coverage = 0
        cnt = 0
        for i in range(len(wrongs)):
            if coverage < wrongs[i][1]:
                cnt += 1
                coverage = wrongs[i][1] + size - 1
                if cnt > sheets:
                    return False

        return True

    else:
        return False


if __name__ == "__main__":
    R, C = map(int, input().split())

    sheets = int(input())
    wrong_cnt = int(input())

    wrongs = list()
    row_max = 0

    for i in range(wrong_cnt):
        a, b = map(int, input().split())
        row_max = max(row_max, a)
        wrongs.append([a, b])

    wrongs.sort(key=lambda x: x[1])

    # print(wrongs)
    start = 1
    end = max(C, R)

    result = 0
    while start <= end:
        mid = (start + end) // 2

        if can_mosaic(mid):
            end = mid - 1
            result = mid

        else:
            start = mid + 1

    print(result)