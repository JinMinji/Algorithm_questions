#Contest340, Q3

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        start = 0
        end = nums[-1] - nums[0]
        while start < end:
            mid = (start+end) // 2
            cnt = 0
            i = 1
            print('mid', mid)
            while i < len(nums):
                if nums[i] - nums[i-1] <= mid:
                    print(mid, i, nums[i], nums[i-1])
                    cnt += 1
                    if cnt >= p:
                        break
                    i += 1
                i += 1
            print('cnt', cnt)
            if cnt >= p:
                end = mid
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    test = Solution()
    # print(test.minimizeMax(nums = [4,2,1,2], p = 1))
    # print(test.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(test.minimizeMax([1, 2], 1))


