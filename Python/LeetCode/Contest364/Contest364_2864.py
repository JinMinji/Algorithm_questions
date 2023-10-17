# Contest364, Q1

from typing import List

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        answer = ""
        one_cnt = 0
        for i in range(len(s)):
            if s[i] == "1":
                one_cnt += 1
        for i in range(one_cnt-1):
            answer += "1"
        answer += "0" * (len(s) - (len(answer) + 1))
        answer += "1"
        return answer
        
if __name__ == "__main__":
    test = Solution()
    print(test.maximumOddBinaryNumber(s = "010"))
    print(test.maximumOddBinaryNumber(s = "0101"))
