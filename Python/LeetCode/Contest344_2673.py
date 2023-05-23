# Contest344, Q4

from typing import List
from math import log


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        level = int(log(n + 1, 2))
        for i in range(1,level):
            for j in range(level):
                
        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.minIncrements(n = 7, cost = [1,5,2,2,3,3,1]))
    print(test.minIncrements(n = 3, cost = [5,3,3]))
    print(test.minIncrements(3, [6410,3594,9382]))
    print(test.minIncrements(15, [764, 1460, 2664, 764, 2725, 4556, 5305, 8829, 5064, 5929, 7660, 6321, 4830, 7055, 3761]))
