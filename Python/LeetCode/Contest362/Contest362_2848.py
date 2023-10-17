# Contest362, Q1

from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cnt = [0 for i in range(101)]
        for i in range(len(nums)):
            a, b = nums[i]
            for k in range(a, b+1):
                cnt[k] = 1
        
        return sum(cnt)
        
if __name__ == "__main__":
    test = Solution()
    print(test.numberOfPoints(nums = [[3,6],[1,5],[4,7]]))
    print(test.numberOfPoints(nums = [[1,3],[5,8]]))
    # print(test.numberOfPoints())
    # print(test.numberOfPoints())
