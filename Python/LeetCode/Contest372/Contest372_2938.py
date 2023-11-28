# Contest372, Q2

from typing import List
from copy import deepcopy

class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = sum(map(int, list(s)))
        white_count = len(s)-black_count
        answer = 0
        next_idx = 0

        for i in range(len(s)):
            if s[i] == '0':
                answer += i - next_idx
                next_idx += 1
                if next_idx == white_count:
                    return answer
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.minimumSteps(s = "101"))
    print(test.minimumSteps(s = "100"))
    print(test.minimumSteps(s = "0111"))
