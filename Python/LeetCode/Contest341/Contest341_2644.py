#Contest341, Q2

from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = 0
        answer = divisors[0]
        for i in range(len(divisors)):
            divisibility_score = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    divisibility_score += 1
            print(divisors[i], divisibility_score)
            if max_score < divisibility_score:
                max_score = divisibility_score
                answer = divisors[i]
            elif max_score == divisibility_score:
                answer = min(answer, divisors[i])
        return answer


if __name__ == "__main__":
    test = Solution()
    # print(test.maxDivScore(nums = [4,7,9,3,9], divisors = [5,2,3]))
    # print(test.maxDivScore(nums = [20,14,21,10], divisors = [5,7,5]))
    # print(test.maxDivScore(nums = [12], divisors = [10,16]))
    # print(test.maxDivScore([56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78], [39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10,33,72,97,60,79,68,25,63]))
    print(test.maxDivScore([4,7,9,3,9], [5,2,3]))

