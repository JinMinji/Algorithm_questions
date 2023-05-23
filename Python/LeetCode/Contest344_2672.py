#Contest344, Q3

from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0 for i in range(n)]
        answer = []
        cnt = 0
        for i in range(len(queries)):
            idx, color = queries[i]
            prev_col, next_col = 0, 0
            origin_col = nums[idx]
            nums[idx] = color
            if idx > 0:
                prev_col = nums[idx-1]
            if idx + 1 < len(nums):
                next_col = nums[idx+1]

            if origin_col == color:
                answer.append(cnt)
                continue

            if origin_col and origin_col == prev_col:
                cnt -= 1
            if origin_col and origin_col == next_col:
                cnt -= 1
            if color == prev_col:
                cnt += 1
            if color == next_col:
                cnt += 1

            answer.append(cnt)

        return answer


if __name__ == "__main__":
    test = Solution()
    print(test.colorTheArray(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]))
    print(test.colorTheArray(n = 1, queries = [[0,100000]]))
    # print(test.colorTheArray())
    # print(test.colorTheArray())


