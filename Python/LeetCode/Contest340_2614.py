#Contest340, Q1

from typing import List

class Solution:
    def isPrime(self, num):
        if num > 1:
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    return False
            return True
        return False

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i][i] > ans and self.isPrime(nums[i][i]):
                ans = nums[i][i]
            if nums[i][len(nums)-i-1] > ans and self.isPrime(nums[i][len(nums)-i-1]):
                ans = nums[i][len(nums)-i-1]

        return ans


if __name__ == "__main__":
    test = Solution()
    nums = [[1, 2, 3], [5, 17, 7], [9, 11, 10]]
    print(test.diagonalPrime(nums))
    nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    print(test.diagonalPrime(nums))


