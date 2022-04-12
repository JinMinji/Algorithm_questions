#여왕벌
import sys

if __name__ == '__main__':
    M, N = map(int, input().split())
    queen_bee = [1 for i in range(2*M-1)]
    result = list()

    for i in range(N):
        nums = list(map(int, sys.stdin.readline().split()))

        for k in range(nums[0], nums[0] + nums[1]):
            queen_bee[k] += 1

        for k in range(nums[0] + nums[1], nums[0] + nums[1] + nums[2]):
            queen_bee[k] += 2

    # print(queen_bee)
    for i in range(M):
        print(queen_bee[M-i-1], ' '.join(map(str, queen_bee[M:])))

