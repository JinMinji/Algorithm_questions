# 회전 초밥

if __name__ == '__main__':
    N, d, k, c = map(int, input().split(' '))

    sushi_list = list()

    for i in range(N):
        sushi_list.append(int(input()))

    sushi_list.extend(sushi_list[:k])   # 이어 붙이기
    print(sushi_list)

    max_res = 0

    pre = 0
    cur_kind = 0

    tmp_kind = [0 for i in range(d + 1)]
    for i in range(k):
        tmp_kind[sushi_list[i]] += 1

    tmp_kind[c] += 1

    max_res = cur_kind

    for i in range(len(tmp_kind)):
        if tmp_kind[i] != 0:
            cur_kind += 1

    for i in range(1, len(sushi_list)-k):
        tmp_kind[pre] -= 1
        if tmp_kind[pre] == 0:
            cur_kind -= 1

        if tmp_kind[sushi_list[i+k-1]] == 0:
            tmp_kind[sushi_list[i+k-1]] += 1
            cur_kind += 1

        max_res = max(max_res, cur_kind)
        print(tmp_kind)
        pre = sushi_list[i]

    print(max_res)