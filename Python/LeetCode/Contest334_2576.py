# Contest 334, Q3
# 문제가 이해가 안됨;

from typing import List


def findPossiblePair(nums: List[int], marked: List[int]):
    global max_num
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and marked[i] == 0 and marked[j] == 0 and 2*nums[i] <= nums[j]:
                marked[i] = 1
                marked[j] = 1
                findPossiblePair(nums, marked)
                marked[i] = 0
                marked[j] = 0

    max_num = max(max_num, sum(marked))


def maxNumOfMarkedIndices(nums: List[int]) -> int:
    global max_num
    max_num = 0
    marked = [0 for i in range(len(nums))]

    findPossiblePair(nums, marked)

    return max_num


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    answer = maxNumOfMarkedIndices(nums)
    print(answer)