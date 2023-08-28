# Contest358, Q1

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        answer = True

        if len(s) != len(words):
            return False
        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.isAcronym(words = ["alice","bob","charlie"], s = "abc"))
    print(test.isAcronym(words = ["an","apple"], s = "a"))
    print(test.isAcronym(words = ["never","gonna","give","up","on","you"], s = "ngguoy"))