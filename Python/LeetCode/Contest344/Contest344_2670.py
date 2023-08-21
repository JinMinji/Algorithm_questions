#Contest344, Q1

from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix_nums = [0 for i in range(51)]
        suffix_nums = [0 for i in range(51)]
        res = []

        for i in range(len(nums)):
            suffix_nums[nums[i]] += 1

        for i in range(len(nums)):
            print(nums[i])
            prefix_nums[nums[i]] += 1
            suffix_nums[nums[i]] -= 1

            res.append(suffix_nums.count(0) - prefix_nums.count(0))

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.distinctDifferenceArray(nums = [1,2,3,4,5]))
    print(test.distinctDifferenceArray(nums = [3,2,3,4,2]))
    # print(test.distinctDifferenceArray())
    # print(test.distinctDifferenceArray())


