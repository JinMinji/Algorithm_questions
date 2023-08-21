#Contest336, Q2

from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cur_score = 0
        answer = 0
        for i in range(len(nums)):
            cur_score += nums[i]
            if cur_score > 0:
                answer += 1
            else:
                break

        return answer

if __name__ == '__main__':
    test = Solution()
    answer = test.maxScore([2,-1,0,1,-3,3,-3])
    print(answer)
    answer = test.maxScore([-2,-3,0])
    print(answer)
    answer = test.maxScore([-687767,-860350,950296,52109,510127,545329,-291223,-966728,852403,828596,456730,-483632,-529386,356766,147293,572374,243605,931468,641668,494446])
    print(answer)