#Contest337, Q4

from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums.sort()
        cnt = [0 for i in range(value)]
        for i in range(len(nums)):
            cnt[nums[i] % value] += 1
        return (min(cnt) * value) + cnt.index(min(cnt))


if __name__ == '__main__':
    test = Solution()
    answer = test.findSmallestInteger([1,-10,7,13,6,8], 5)
    print(answer)
    answer = test.findSmallestInteger([1,-10,7,13,6,8], 7)
    print(answer)