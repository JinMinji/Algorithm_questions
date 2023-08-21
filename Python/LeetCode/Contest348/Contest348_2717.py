# Contest348, Q2

from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        min_index = nums.index(1)
        max_index = nums.index(len(nums))
        answer = min_index + len(nums) - 1 - max_index
        if min_index > max_index:
            answer -= 1

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.semiOrderedPermutation(nums = [2,1,4,3]))
    print(test.semiOrderedPermutation(nums = [2,4,1,3]))
    print(test.semiOrderedPermutation(nums = [1,3,4,2,5]))
    print(test.semiOrderedPermutation(nums=[4,2,3,1]))
    print(test.semiOrderedPermutation(nums=[3, 2, 1]))

