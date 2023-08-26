# Contest351, Q3

from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        answer = 1
        before_one = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if before_one >= 0:
                    answer *= i - before_one
                    answer %= 10**9 + 7
                before_one = i

        if before_one == -1:
            return 0
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.numberOfGoodSubarraySplits(nums = [0,1,0,0,1]))
    print(test.numberOfGoodSubarraySplits(nums = [0,1,0]))
    # print(test.makeTheIntegerZero())
