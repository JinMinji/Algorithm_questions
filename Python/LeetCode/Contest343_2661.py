#Contest343, Q2

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = [len(mat[0]) for i in range(len(mat))]
        cols = [len(mat) for i in range(len(mat[0]))]
        loc_dic = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                loc_dic[mat[i][j]] = [i, j]

        for i in range(len(arr)):
            x, y = loc_dic[arr[i]]
            rows[x] -= 1
            cols[y] -= 1
            if rows[x] == 0 or cols[y] == 0:
                return i


if __name__ == "__main__":
    test = Solution()
    print(test.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
    print(test.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))
    # print(test.firstCompleteIndex())
    # print(test.firstCompleteIndex())
