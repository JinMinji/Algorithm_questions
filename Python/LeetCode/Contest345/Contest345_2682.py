# Contest345, Q1

from typing import List
from math import log


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friends = [1 for i in range(n)]
        cur = 0
        for i in range(1, n+1):
            friends[cur] = 0
            cur = (cur + i * k) % n
            if friends[cur] == 0:
                break

        answer = []
        for i in range(n):
            if friends[i] == 1:
                answer.append(i+1)
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.circularGameLosers(n = 5, k = 2))
    print(test.circularGameLosers(n = 4, k = 4))