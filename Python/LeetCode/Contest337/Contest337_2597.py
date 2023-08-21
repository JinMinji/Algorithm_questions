#Contest337, Q3

from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = 0
        nums.sort()
        print(nums)
        for n in range(1, 2**len(nums)):
            cur = str(bin(n))[2:].zfill(len(nums))
            flag = True
            k_nums = []
            for i in range(len(nums)):
                if cur[i] == '1':
                    k_nums.append(nums[i]+k)
            for i in range(len(nums)):
                if cur[i] == '1' and nums[i] in k_nums:
                    flag = False
                    break
            if flag:
                result += 1

        return result


if __name__ == '__main__':
    test = Solution()
    answer = test.beautifulSubsets([2,4,6], 2)
    print(answer)
    answer = test.beautifulSubsets([10,4,5,7,2,1], 3)
    print(answer)
    answer = test.beautifulSubsets([4,2,5,9,10,3], 1)
    print(answer)
    # answer = test.beautifulSubsets([20,14,22,1,4,11,21,19,29,25,12,18,9,15,23,6,27,16,26,5], 13)
    # print(answer)
    answer = test.beautifulSubsets([15,6,3,25,14,29,21,16,28,23,11,9,4,30,24,12,26,1,27,18], 7)
    print(answer)