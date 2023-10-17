# Contest365, Q3

from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        target %= sum(nums)
        for i in range(len(nums)):
            
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.minSizeSubarray(nums = [1,2,3], target = 5))
    print(test.minSizeSubarray(nums = [1,1,1,2,3], target = 4))
    print(test.minSizeSubarray(nums = [2,4,6,8], target = 3))
