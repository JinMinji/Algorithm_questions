# Contest365, Q2

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        cur_max = 0
        cur_min = 10**5
        cur_i = 0
        cur_j = 0
        for i in range(len(nums)-2):
            cur_max = max(cur_max, nums[i])
            if cur_max < nums[i]:
                cur_i = i
            for j in range(i+1, len(nums)-1):
                cur_min = min(cur_min, nums[j])
                if cur_min > nums[j]:
                    cur_j = j
                    print(cur_i, cur_j)
                answer = max(answer, (cur_max-cur_min) * max(nums[j+1:]))
                
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumTripletValue(nums = [12,6,1,2,7]))
    print(test.maximumTripletValue(nums = [1,10,3,4,19]))
    print(test.maximumTripletValue(nums = [1,2,3]))
    print(test.maximumTripletValue(nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]))
