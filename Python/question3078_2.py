# 좋은 친구 골드 3
from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split(' '))

    name_sum_list = [0 for i in range(21)]  # 이름 글자수 최대 20자. 글자 수 별 인원 합을 가지고 있다.
    name_len_list = deque()      #
    result = 0

    for i in range(K+1):
        n = len(input())
        result += name_sum_list[n]
        name_len_list.append(n)
        name_sum_list[n] += 1

    for i in range(K+1, N):
        del_num = name_len_list.popleft()
        name_sum_list[del_num] -= 1

        n = len(input())
        result += name_sum_list[n]
        name_len_list.append(n)
        name_sum_list[n] += 1

    print(result)