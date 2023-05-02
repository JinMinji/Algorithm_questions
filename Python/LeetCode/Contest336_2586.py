#Contest336, Q1

from typing import List

class Solution:
    def vowelStrings(self,  words: List[str], left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right+1):
            if words[i][0] in ['a', 'e', 'i', 'o', 'u'] and words[i][-1] in ['a', 'e', 'i', 'o', 'u']:
                cnt += 1

        return cnt


if __name__ == '__main__':
    test = Solution()
    answer = test.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4)
    print(answer)
    answer = test.vowelStrings(["are","amy","u"], 0, 2)
    print(answer)