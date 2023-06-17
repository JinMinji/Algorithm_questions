# Contest349, Q1

from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] != min(nums) and nums[i] != max(nums):
                return nums[i]
        return -1

if __name__ == "__main__":
    test = Solution()
    print(test.findNonMinOrMax(nums = [3,2,1,4]))
    print(test.findNonMinOrMax(nums = [1,2]))
    print(test.findNonMinOrMax(nums = [2,1,3]))