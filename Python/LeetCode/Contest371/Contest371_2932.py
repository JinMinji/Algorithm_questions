# Contest371, Q1

from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    answer = max(answer, nums[i]^nums[j])
        return answer
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumStrongPairXor(nums = [1,2,3,4,5]))
    print(test.maximumStrongPairXor(nums = [10,100]))
    print(test.maximumStrongPairXor(nums = [5,6,25,30]))
