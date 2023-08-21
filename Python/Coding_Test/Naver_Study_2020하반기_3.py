# 성냥개비
from itertools import permutations
cnt_num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
how_can = [0, 0, 1, 1, 1, 3, 3, 1]
dp = [-1 for i in range(51)]
dp_list = [[] for i in range(51)]

temp = [2, 2, 4]

print(list(set(list(permutations(temp, 3)))))

def dp(k):
    if dp[k] != -1:
        return dp[k]

    else:
        if k % 2 == 0:  # 짝수 최소 2
            pass
        else :   #홀수, 최소 3
            for i in range(8):
                pass


def solutions(k):
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp_list[2] = [(1)]
    dp[3] = 1
    dp_list[3] = [(7)]
    dp[4] = 2
    dp_list[4] = [(4), (1, 1)]
    dp[5] = 5
    dp_list[5] = [(2), (3), (5), (1, 7), (7, 1)]
    dp[6] = 7
    dp_list[6] = [(0), (6), (9), (7, 7), (1, 4), (4, 1), (1, 1, 1)]
    dp[7] = 12
    dp_list[7] = [(8), (4, 7), (7, 4), (1, 1, 7), (1, 7, 1), (7, 1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (1, 5), (5, 1)]
    dp[8] = 15
    dp_list[8] = [(1, 0), (0, 1), (1, 6), (6, 1), (1, 9), (9, 1), (7, 2), (7, 3), (3, 7), (7, 5), (5, 7), (4, 4), (1, 1, 4), (4, 1, 1), (1, 4, 1)]

    answer = dp(k)
    return answer


# if __name__ == '__main__':
#     print(solutions(5))
#     print(solutions(6))
#     print(solutions(7))
#     # print(solutions(11))
#     print(solutions(1))
#
#
