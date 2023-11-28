# Contest372, Q1

from typing import List

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_len = min(len(s1), len(s2), len(s3))
        for i in range(min_len):
            if s1[i] == s2[i] == s3[i]:
                continue
            if i < 1:
                return -1
            return len(s1)+len(s2)+len(s3)-(3*i) 
        return len(s1)+len(s2)+len(s3)-(3*(min_len))
    
if __name__ == "__main__":
    test = Solution()
    # print(test.findMinimumOperations(s1 = "abc", s2 = "abb", s3 = "ab"))
    # print(test.findMinimumOperations(s1 = "dac", s2 = "bac", s3 = "cac"))
    print(test.findMinimumOperations(s1 = "ca", s2 = "cccabb", s3 = "cb"))
