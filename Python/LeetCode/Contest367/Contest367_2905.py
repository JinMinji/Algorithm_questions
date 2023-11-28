# Contest367, Q3

from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)-indexDifference):
            for j in range(i+indexDifference, len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j] 
        return [-1, -1]
        
if __name__ == "__main__":
    test = Solution()
    print(test.findIndices(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
    print(test.findIndices(nums = [2,1], indexDifference = 0, valueDifference = 0))
    print(test.findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))
