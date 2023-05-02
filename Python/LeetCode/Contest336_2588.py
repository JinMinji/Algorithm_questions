#Contest336, Q3

from typing import List

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        for n in range(2, len(nums)):
            # n개 의 배열
            sum_subarr = sum(nums[:n])
            if sum_subarr % 2 == 0:
                cnt += 1
            for i in range(len(nums) - n):
                sum_subarr = sum_subarr - nums[i] + nums[i+n]
                if sum_subarr % 2 == 0:
                    print(n, i, sum_subarr)
                    cnt += 1

        return cnt


if __name__ == '__main__':
    test = Solution()
    answer = test.beautifulSubarrays([4,3,1,2,4])
    print(answer)
    answer = test.beautifulSubarrays([1,10,4])
    print(answer)
