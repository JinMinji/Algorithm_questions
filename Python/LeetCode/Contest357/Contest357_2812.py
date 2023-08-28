# Contest357, Q3

from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        answer = 0


        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.maximumSafenessFactor(grid = [[1,0,0],[0,0,0],[0,0,1]]))
    print(test.maximumSafenessFactor(grid = [[0,0,1],[0,0,0],[0,0,0]]))
    print(test.maximumSafenessFactor(grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))