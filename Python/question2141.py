# 우체국, 골드4
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    # N은 최대 10만.
    # 10만번만 도는 거면 그것도 괜찮다.

    # 누적합.
    villages = list()
    for i in range(N):
        villages.append(list(map(int, sys.stdin.readline().split())))

    villages.sort()
    # 어차피 정답이되는 장소는 어떤 마을의 위일라나..?
    prefix_num = [[0, 0] for i in range(N)]
    left_cnt = villages[0][1]
    right_cnt = villages[-1][1]
    for i in range(1, N):
        # print(left_cnt, right_cnt)
        prefix_num[i][0] = prefix_num[i - 1][0] + abs(villages[i][0] - villages[i - 1][0]) * left_cnt
        left_cnt += villages[i][1]
        tmp_idx = N - i
        prefix_num[tmp_idx - 1][1] = prefix_num[tmp_idx][1] + abs(
            villages[tmp_idx][0] - villages[tmp_idx - 1][0]) * right_cnt
        right_cnt += villages[tmp_idx - 1][1]

    tmp_min = float('inf')
    answer = 0
    for i in range(N):
        if sum(prefix_num[i]) < tmp_min:
            tmp_min = sum(prefix_num[i])
            answer = i

    # print(prefix_num)
    print(villages[answer][0])