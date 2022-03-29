#사전, 골드3
from itertools import combinations

if __name__ =='__main__':
    N, M, K = map(int, input().split(' '))
    # 총 길이 N + M
    # N + M 개 중에, N개를 순서에 상관없이 뽑아서, 정렬.
    a_pos_list = combinations([i for i in range(N+M)], N)

    a_pos_list = list(a_pos_list)
    # print(a_pos_list)

    a_pos_list.sort()

    tmp_list = ['z' for i in range(N+M)]

    if len(a_pos_list) <= K:
        print(-1)
    else:
        for i in a_pos_list[K-1]:
            tmp_list[i] = 'a'

        print(''.join(tmp_list))