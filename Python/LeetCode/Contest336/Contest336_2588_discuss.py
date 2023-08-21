#Contest336, Q3

from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        cur = 0
        cnt = 0
        for i in range(len(nums)):
            cur ^= nums[i]
            cnt += dp[cur]
            if cur == 0:
                cnt += 1
            dp[cur] += 1
        return cnt


if __name__ == '__main__':
    test = Solution()
    answer = test.beautifulSubarrays([4,3,1,2,4])
    print(answer)
    answer = test.beautifulSubarrays([1,10,4])
    print(answer)
