#Contest339, Q2

from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pre = 0
        cur_row = 0
        result = [[]]
        for i in range(len(nums)):
            if nums[i] == pre:
                cur_row += 1
                if len(result) > cur_row:
                    result[cur_row].append(nums[i])
                else:
                    result.append([nums[i]])
            else:
                cur_row = 0
                result[0].append(nums[i])
                pre = nums[i]
        return result


if __name__ == '__main__':
    test = Solution()
    answer = test.findMatrix(nums = [1,3,4,1,2,3,1])
    print(answer)
    answer = test.findMatrix(nums = [1,2,3,4])
    print(answer)