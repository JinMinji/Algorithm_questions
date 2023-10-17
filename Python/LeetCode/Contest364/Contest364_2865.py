# Contest364, Q2

from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        answer = 0
        for i in range(len(maxHeights)):
            # if i is peak.
            cur_total = maxHeights[i]
            pre_max = maxHeights[i]
            for j in range(1, i+1):
                pre_max = min(pre_max, maxHeights[i-j])
                cur_total += pre_max
            pre_max = maxHeights[i]
            for k in range(i+1, len(maxHeights)):
                pre_max = min(pre_max, maxHeights[k])
                cur_total += pre_max
            answer = max(answer, cur_total)
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumSumOfHeights(maxHeights = [5,3,4,1,1]))
    print(test.maximumSumOfHeights(maxHeights = [6,5,3,9,2,7]))
    print(test.maximumSumOfHeights(maxHeights = [3,2,5,5,2,3]))
