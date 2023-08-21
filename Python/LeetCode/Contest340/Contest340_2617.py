#Contest340, Q4

from typing import List
from collections import deque

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        visited_i = [[i for i in range(len(grid))] for j in range(len(grid[0]))]
        visited_j = [[j for j in range(len(grid[0]))] for i in range(len(grid))]
        visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        visited[0][0] = 1
        to_visit = deque()
        to_visit.append((0, 0, 1))
        n = len(grid)
        m = len(grid[0])
        target = (n - 1, m - 1)
        # print('target idx', len(grid) - 1, len(grid[0]) - 1)
        while to_visit:
            i, j, cnt = to_visit.popleft()
            # print(i, j, cnt)
            if (i, j) == target:
                return cnt
            for k in range(j+1, min(j + grid[i][j] + 1, m)):
                if visited[i][k]:
                    continue
                visited[i][k] = 1
                to_visit.append((i, k, cnt+1))
            for k in range(i+1, min(i + grid[i][j] + 1, n)):
                if visited[k][j]:
                    continue
                visited[k][j] = 1
                to_visit.append((k, j, cnt+1))
        return -1


if __name__ == "__main__":
    test = Solution()
    print(test.minimumVisitedCells(grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
    print(test.minimumVisitedCells(grid = [[2,1,0],[1,0,0]]))


