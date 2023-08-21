# 별 찍기 - 11, 골드 4 - 맞은 버전
import math

basic_star = [[' ', ' ', '*', ' ', ' ', ' '],
              [' ', '*', ' ', '*', ' ', ' '],
              ['*', '*', '*', '*', '*', ' ']]


def merge_triangle(star_arr):
    result_arr = [[' ' for i in range(len(star_arr[0])*2)] for j in range(len(star_arr)*2)]

    H = len(star_arr)
    W = len(star_arr[0])

    # 3번 복사해야함.
    # 맨 위 삼각형
    for i in range(len(star_arr)):
        for j in range(len(star_arr[0])):
            # 3번 복사해야함.
            # 맨 위 삼각형
            result_arr[i][W//2+j] = star_arr[i][j]
            # 왼쪽 아래 삼각형
            result_arr[H + i][j] = star_arr[i][j]
            # 오른쪽 아래 삼각형
            result_arr[H + i][W + j] = star_arr[i][j]

    return result_arr


if __name__ == '__main__':
    N = int(input())

    K = int(math.log2(N//3))

    result = basic_star

    for i in range(K):
        result = merge_triangle(result)

    for r in range(len(result)):
        print(''.join(result[r]))

