# Contest364, Q3

from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        #누적합이겟지 뭐,
        cur_left_total = 0
        cur_right_total = maxHeights[0]
        pre_max = maxHeights[0]
        for i in range(1, len(maxHeights)):
            pre_max = min(pre_max, maxHeights[i])
            cur_right_total += pre_max
        
        answer = cur_left_total + cur_right_total

        
        for i in range(1, len(maxHeights)):
            cur
            answer = max(answer, cur_left_total + cur_right_total)

        return answer
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumSumOfHeights(maxHeights = [5,3,4,1,1]))
    print(test.maximumSumOfHeights(maxHeights = [6,5,3,9,2,7]))
    print(test.maximumSumOfHeights(maxHeights = [3,2,5,5,2,3]))
