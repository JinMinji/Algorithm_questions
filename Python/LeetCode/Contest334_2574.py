# contest 334, Q1
from typing import List

def leftRigthDifference(nums: List[int]) -> List[int]:
    left_sum = 0
    right_sum = sum(nums)
    result = []
    for i in range(len(nums)):
        right_sum -= nums[i]
        result.append(abs(right_sum - left_sum))
        left_sum += nums[i]

    return result


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    answer = leftRigthDifference(nums)

    print(answer)