# Contest352, Q1

from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        answer = 0

        isOdd = False
        start_idx = -1
        for i in range(len(nums)):
            if nums[i] > threshold: # 최댓값 체크
                if start_idx != -1:
                    answer = max(i-start_idx, answer)
                start_idx = -1
                continue
            if start_idx == -1 and nums[i] % 2 == 0:    #시작은 짝수에서 가능.
                start_idx = i
                isOdd = False if nums[i] % 2 == 0 else True
            elif start_idx != -1:
                if (nums[i] % 2 == 0) == isOdd:
                    isOdd = not isOdd
                else:
                    answer = max(i - start_idx, answer)
                    if nums[i] % 2 != 0:
                        start_idx = -1
                    else:
                        start_idx = i
                        isOdd = False

        if start_idx != -1:
            answer = max(len(nums)-start_idx, answer)

        return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
    # print(test.longestAlternatingSubarray(nums = [1,2], threshold = 2))
    # print(test.longestAlternatingSubarray(nums = [2,3,4,5], threshold = 4))
    print(test.longestAlternatingSubarray(nums=[4,10,3], threshold=10))
