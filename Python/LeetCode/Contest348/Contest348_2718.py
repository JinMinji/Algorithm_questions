# Contest348, Q3

from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rows = [0 for i in range(n)]
        row_cnt = n
        cols = [0 for i in range(n)]
        col_cnt = n

        answer = 0
        for i in range(len(queries)-1, -1, -1):
            t, idx, val = queries[i]
            if t:
                if rows[idx]:
                    continue
                rows[idx] = 1
                row_cnt -= 1
                answer += val*col_cnt

            else:
                if cols[idx]:
                    continue
                cols[idx] = 1
                col_cnt -= 1
                answer += val * row_cnt

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.matrixSumQueries(n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]))
    print(test.matrixSumQueries(n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]))
    print(test.matrixSumQueries(n = 2, queries = [[1,1,1],[1,0,7],[0,0,0]]))