# Contest355, Q1

from typing import List

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        tmp = []
        for i in range(len(words)):
            tmp.extend(words[i].split(separator))

        for w in tmp:
            if w == '':
                continue
            answer.append(w)

        return answer

if __name__ == "__main__":
    test = Solution()
    print(test.splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
    print(test.splitWordsBySeparator(words = ["$easy$","$problem$"], separator = "$"))
    print(test.splitWordsBySeparator( words = ["|||"], separator = "|"))