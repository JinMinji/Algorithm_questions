#Contest338, Q2

from typing import List

class Solution:
    def findMinimumPrime(self, gap, max_num):
        for i in range(max(2, gap+1), max_num):
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                print(gap, max_num, 'return', i)
                return i
        return max_num

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            print('check', nums[-i], nums[-(i+1)])
            if nums[-i] > nums[-(i+1)]:
                continue
            gap = nums[-(i+1)] - nums[-i]
            print('gap', gap)
            subtract_prime = self.findMinimumPrime(gap, nums[-(i+1)])
            nums[-(i+1)] -= subtract_prime
            if nums[-(i+1)] <= 0:
                return False
        return True


if __name__ == '__main__':
    test = Solution()
    # answer = test.primeSubOperation([4,9,6,10])
    # print(answer)
    # answer = test.primeSubOperation([6,8,11,12])
    # print(answer)
    # answer = test.primeSubOperation([5,8,3])
    # print(answer)
    answer = test.primeSubOperation([2,2])
    print(answer)