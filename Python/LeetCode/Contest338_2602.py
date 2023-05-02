#Contest338, Q3

from typing import List

class Solution:
    def binsearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        idx = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                idx = mid
                print(mid, target, nums[mid])
                start = mid + 1
            else:
                end = mid - 1
        return idx

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        answer = [0 for i in range(len(queries))]
        nums.sort()
        prefix_sum = [0 for i in range(len(nums))]
        prefix_sum[0] = nums[0]
        idxs = [-1 for i in range(len(queries))]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        print(prefix_sum)
        print(nums)
        for i in range(len(queries)):
            idx = self.binsearch(nums, queries[i])
            print('idx', idx)
            if idx != -1:
                left_cnt = queries[i]*(idx+1) - prefix_sum[idx]
                right_cnt = (prefix_sum[-1] - prefix_sum[idx]) - queries[i] * (len(nums) - (idx+1))
                answer[i] = left_cnt + right_cnt
                print('left', left_cnt)
                print('right', right_cnt)
            else:
                answer[i] = prefix_sum[-1] - (queries[i] * len(nums))

        return answer


if __name__ == '__main__':
    test = Solution()
    answer = test.minOperations(nums = [3,1,6,8], queries = [1,5])
    print(answer)
    answer = test.minOperations(nums =[47,50,97,58,87,72,41,63,41,51,17,21,7,100,69,66,79,92,84,9,57,26,26,28,83,38],
                                queries =[3])
    print(answer)