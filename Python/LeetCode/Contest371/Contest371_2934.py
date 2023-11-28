# Contest371, Q3

from typing import List
from copy import deepcopy

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums_2_1 = deepcopy(nums1)
        nums_2_2 = deepcopy(nums2)
        answer1 = 0
        if nums1[-1] > nums2[-1]:
            nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
            answer1 += 1
        print(nums1, nums2)
        for i in range(len(nums1)-1):
            print(nums1[i], nums2[i])
            if nums1[i] > nums2[i] and nums1[i] > nums1[-1]:
                answer1 += 1
                nums1[i], nums2[i] = nums2[i], nums1[i]
            if nums1[i] > nums1[-1] or nums2[i] > nums2[-1]:
                answer1 = -1
                break
        

        print(nums_2_1, nums_2_2)
        answer2 = 0
        if nums_2_2[-1] > nums_2_1[-1]:
            nums_2_2[-1], nums_2_1[-1] = nums_2_1[-1], nums_2_2[-1]
            answer2 += 1
        print(nums_2_2, nums_2_1)
        for i in range(len(nums_2_2)-1):
            print(nums_2_2[i], nums_2_1[i])
            if nums_2_2[i] > nums_2_1[i] and nums_2_2[i] > nums_2_2[-1]:
                answer2 += 1
                nums_2_2[i], nums_2_1[i] = nums_2_1[i], nums_2_2[i]
            if nums_2_2[i] > nums_2_2[-1] or nums_2_1[i] > nums_2_1[-1]:
                answer2 = -1
                break

        return min(answer1, answer2)
        
        
if __name__ == "__main__":
    test = Solution()
    # print(test.minOperations(nums1 = [1,2,7], nums2 = [4,5,3]))
    # print(test.minOperations(nums1 = [2,3,4,5,9], nums2 = [8,8,4,4,4]))
    # print(test.minOperations(nums1 = [1,5,4], nums2 = [2,5,3]))
    print(test.minOperations(nums1 = [1,5,15], nums2 = [1,1,1]))
