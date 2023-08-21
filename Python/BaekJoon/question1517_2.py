# 20210527 버블소트
import heapq

swap_cnt = 0

def merge(l_list, r_list):
    global swap_cnt
    result = []

    while len(l_list) > 0 or len(r_list) > 0:
        if len(l_list) > 0 and len(r_list) > 0:
            if l_list[0] < r_list[0]:
                result.append(l_list.pop(0))
            else:
                result.append(r_list.pop(0))
                swap_cnt += len(l_list)  # 오른쪽에 있는게 앞으로 오니까!
        elif len(r_list) == 0:
            result.append(l_list.pop(0))
        else:
            result.append(r_list.pop(0))

    return result

def merge_sort(nlist):  #1/2 n
    if len(nlist) <= 1:
        return nlist

    mid = len(nlist) // 2
    leftList = nlist[:mid]
    rightList = nlist[mid:]

    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)

if __name__ == "__main__":
    N = int(input())
    num_list = list(map(int, input().split(' ')))
    merge_sort(num_list)

    print(swap_cnt)