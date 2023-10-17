# Contest363, Q1

from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                answer += nums[i]

        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1))
    print(test.sumIndicesWithKSetBits(nums = [4,3,2,1], k = 2))
