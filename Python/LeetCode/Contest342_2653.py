#Contest342, Q3

from typing import List
from collections import deque

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cur = nums[:k]
        for i in range(len(nums)-(k-1)):




if __name__ == "__main__":
    test = Solution()
    print(test.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2))
    print(test.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2))
    print(test.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))


