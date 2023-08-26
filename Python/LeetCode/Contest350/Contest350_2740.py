# Contest350, Q2

from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        answer = nums[-1]
        for i in range(1, len(nums)):
            answer = min(answer, nums[i] - nums[i-1])
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.findValueOfPartition(nums = [1,3,2,4]))
    print(test.findValueOfPartition(nums = [100,1,10]))
    # print(test.minCost())
