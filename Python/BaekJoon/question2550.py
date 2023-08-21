#전구, 골드3
import copy

if __name__ == "__main__":
    N = int(input())

    tmp_lst = list(map(int, input().split()))
    switch = list(map(int, input().split()))

    for i in range(N):
        tmp = switch[i]
        switch[i] = tmp_lst.index(tmp)

    # print(switch)
    max_switch = [[switch[i]] for i in range(N)]
    tmp_len = [0 for i in range(N)]
    for i in range(1, N):
        for j in range(i):
            if switch[j] < switch[i]:
                # print(j, switch[j], i, switch[i])
                if len(max_switch[i]) < len(max_switch[j]) + 1:
                    max_switch[i] = copy.deepcopy(max_switch[j])
                    max_switch[i].append(switch[i])
                    tmp_len[i] = len(max_switch[i])

    # print(max_switch)
    # print(tmp_len)
    result_len = max(tmp_len)
    result_lst = max_switch[tmp_len.index(result_len)]

    # print(result_len)

    for i in range(result_len):
        result_lst[i] = str(tmp_lst[result_lst[i]])

    result_lst.sort()
    print(" ".join(map(str, result_lst)))
    # for i in range(result_len):
    #     print(result_lst[i], end= " ")