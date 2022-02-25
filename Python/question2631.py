# 줄세우기

if __name__ == '__main__':
    N = int(input())

    children_queue = list()

    gap_list = list()

    gap_max = 0

    gap_max_list = list()

    for i in range(N):
        children_queue.append(int(input()))
        gap_list.append(abs(i+1-children_queue[i]))

        if gap_list[i] != 0 and gap_max < gap_list[i] :
            gap_max = gap_list[i]
            gap_max_list = [gap_list[i]]

        elif gap_max == gap_list[i]:
            gap_max_list.append(gap_list[i])

    result = 0

    while any(gap_list):    # 0이 아닌게 하나라도 있으면, 마저 정렬

        gap_list.append(abs(i + 1 - children_queue[i]))


    print(result)