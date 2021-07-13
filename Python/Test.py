def lower_bound(h, height_list):
    start = 0
    end = len(height_list)
    while start <= end:
        mid = (start + end) // 2
        if height_list[mid] <= h:
            start = mid+1
        else:
            end = mid-1
    return len(height_list[end:])

N, M = 3, 5

melting_cnt = [[0 for i in range(M)] for j in range(N)]

print(melting_cnt)
