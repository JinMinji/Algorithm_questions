#Contest340, Q2

from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = [0 for i in range(len(nums))]
        same_val = defaultdict(list)
        for i in range(len(nums)):
            same_val[nums[i]].append(i)

        for value in same_val.values():
            n = len(value)
            left_sum = 0
            right_sum = sum(value)
            for j in range(len(value)):
                arr[value[j]] = right_sum - (n - j) * value[j] + j * value[j] - left_sum
                left_sum += value[j]
                right_sum -= value[j]

        return arr


if __name__ == "__main__":
    test = Solution()
    print(test.distance(nums = [1,3,1,1,2]))
    print(test.distance(nums = [0,5,3]))


