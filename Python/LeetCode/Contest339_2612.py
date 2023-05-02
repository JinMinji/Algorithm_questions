#Contest339, Q4

from typing import List

class Solution:
    def findMinCnt(self, curCnt, k, curP, n, ans):
        INF = 10**5
        pre = -1
        for i in range(curP-k+1, curP):
            if pre == -1:
                if ans[i] != -1:
                    ans[i] = curCnt + 1
                    self.findMinCnt(curCnt+1, k, i, n, ans)
            else:
                if i < 0 or i+k >= n:
                    continue
            ans[pre + 2]
            pre = i

    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        INF = 10**5
        ans = [INF for i in range(n)]
        ans[p] = 0
        for i in range(len(banned)):
            ans[banned[i]] = -1

        to_visit = [(0, p)]
        while to_visit:
            for i in range(curP - k + 1, curP):
                if pre == -1:
                    if ans[i] != -1:
                        ans[i] = curCnt + 1
                        self.findMinCnt(curCnt + 1, k, i, n, ans)
                else:
                    if i < 0 or i + k >= n:
                        continue

        self.findMinCnt(0, )


if __name__ == '__main__':
    test = Solution()
    answer = test.minReverseOperations(n = 4, p = 0, banned = [1,2], k = 4)
    print(answer)
    answer = test.minReverseOperations(n = 5, p = 0, banned = [2,4], k = 3)
    print(answer)
    answer = test.minReverseOperations(n = 4, p = 2, banned = [0,1,3], k = 1)
    print(answer)