# Contest370, Q1

from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        winner = -1
        for i in range(len(grid)):
            if sum(grid[i]) == len(grid)-1:
                winner = i
                break
        return winner
    
if __name__ == "__main__":
    test = Solution()
    print(test.findChampion(grid = [[0,1],[0,0]]))
    print(test.findChampion(grid = [[0,0,1],[1,0,1],[0,0,0]]))
    print(test.findChampion([[0,1],[1,2]]))
