# Contest347, Q2

from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        answer = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                top_left, bottom_right = [], []
                # print('here', i, j)
                for k in range(1, min(i, j)+1):
                    # print('top', k)
                    top_left.append(grid[i-k][j-k])
                for k in range(1, min(len(grid)-i, len(grid[0])-j)):
                    # print('bottom', k)
                    bottom_right.append(grid[i+k][j+k])

                # print(i, j, top_left, bottom_right)
                top_left = set(top_left)
                bottom_right = set(bottom_right)
                answer[i][j] = abs(len(top_left) - len(bottom_right))

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.differenceOfDistinctValues(grid = [[1,2,3],[3,1,5],[3,2,1]]))
    print(test.differenceOfDistinctValues(grid = [[1]]))