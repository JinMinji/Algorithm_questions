#Contest341, Q1

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [-1, -1]
        for i in range(len(mat)):
            if answer[1] < sum(mat[i]):
                answer = [i, sum(mat[i])]

        return answer

if __name__ == "__main__":
    test = Solution()
    print(test.rowAndMaximumOnes([[0,0,0],[0,1,1]]))
    print(test.rowAndMaximumOnes([[0,1],[1,0]]))


