# Contest351, Q1

from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        first = []
        last = []
        for i in range(len(nums)):
            first.append(int(str(nums[i])[0]))
            last.append(int(str(nums[i])[-1]))
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(first[i], last[j]) == 1:
                    answer += 1

        return answer

if __name__ == "__main__":
    test = Solution()
    print(test.countBeautifulPairs(nums = [2,5,1,4]))
    print(test.countBeautifulPairs(nums = [11,21,12]))
    # print(test.countBeautifulPairs())
