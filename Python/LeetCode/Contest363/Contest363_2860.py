# Contest363, Q2

from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()

        for i in range(len(nums)-1):
            # nums[i] 를 선택했을 때
            # 선택 학생들 합 > nums[i]
            # nums[i] 를 선택하지 않았을 때
            # 선택 학생들 합 < nums[i]
            answer += nums[i] < i+1 and nums[i+1] > i+1
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.countWays(nums = [1,1]))
    print(test.countWays(nums = [6,0,3,3,6,7,2,7]))
    # print(test.countWays())
    # print(test.countWays())
