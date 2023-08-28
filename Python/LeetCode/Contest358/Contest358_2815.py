# Contest358, Q1

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = -1
        max_nums = [[] for i in range(10)]
        for i in range(len(nums)):
            max_nums[int(max(str(nums[i])))].append(nums[i])

        for i in range(len(max_nums)):
            max_nums[i].sort(reverse=True)
            if len(max_nums[i]) > 1:
                answer = max(answer, max_nums[i][0] + max_nums[i][1])

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.maxSum(nums = [51,71,17,24,42]))
    print(test.maxSum(nums = [1,2,3,4]))
    # print(test.maxSum(nums = [2,1,3]))