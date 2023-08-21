#Contest337, Q2

from typing import List

class Solution:
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        cur = [0, 0]
        n = len(grid)
        cur_step = 0
        if grid[0][0] != 0:
            return False
        for k in range(n*n-1):
            i, j = cur
            for d in range(8):
                x = i + self.dx[d]
                y = j + self.dy[d]
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == grid[i][j]+1:
                        cur = [x, y]
                        cur_step += 1
                        print(cur_step, x, y)
                        break
            if cur_step != k+1:
                return False

        return True


if __name__ == '__main__':
    test = Solution()
    answer = test.checkValidGrid([[0,3,6],[5,8,1],[2,7,4]])
    print(answer)

    answer = test.checkValidGrid([[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]])
    print(answer)

    answer = test.checkValidGrid([[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]])
    print(answer)
