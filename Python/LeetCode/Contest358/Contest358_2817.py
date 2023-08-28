# Contest358, Q3

from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        answer = abs(nums[0]-nums[x])
        nums_cnt = [0 for i in range(10**2+1)]

        # 이분 탐색?

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.minAbsoluteDifference(nums = [4,3,2,4], x = 2))
    # print(test.minAbsoluteDifference(nums = [5,3,2,10,15], x = 1))
    print(test.minAbsoluteDifference(nums = [1,2,3,4], x = 3))