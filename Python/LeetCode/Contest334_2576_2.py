# Contest 334, Q3
# 두번째 풀이, greedy

from typing import List

def maxNumOfMarkedIndices(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    mid = len(nums) // 2
    marked = 0
    left = 0
    right = mid
    while left < mid:
        if 2 * sorted_nums[left] <= sorted_nums[right]:
            marked += 2
            left += 1
        right += 1
        if right >= len(nums):
            break
    return marked


if __name__ == '__main__':
    # nums = list(map(int, input().split()))
    answer = maxNumOfMarkedIndices([9, 2, 3, 4])
    print(answer)