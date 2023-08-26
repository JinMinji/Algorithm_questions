# Contest355, Q1

from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        answer = 0
        cur = 0
        for i in range(1, len(nums)+1):
            if cur >= nums[-i]:
                cur += nums[-i]
            else:
                answer = max(answer, cur)
                cur = nums[-i]
        answer = max(answer, cur)

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.maxArrayValue(nums = [2,3,7,9,3]))
    print(test.maxArrayValue(nums = [5,3,3]))