#Contest335, Q4

from typing import List

class Solution:
    dp_arr = [-1 for i in range(1001)]
    cnt = [0 for i in range(51)]

    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        self.dp_arr[0] = 1
        for i in range(len(types)):
            self.cnt[types[i][1]] = types[i][0]
            for j in range(target, -1, -1):
                for k in range(types[i][0]):
                    if j - k * types[i][0] >= 0:
                        self.dp_arr[j] += self.dp_arr[j - k * types[i][0]]
                        self.dp_arr[j] %= (10**9 + 7)

        return self.dp_arr[target]


if __name__ == '__main__':
    test = Solution()
    answer = test.waysToReachTarget(18, [[6,1],[3,2],[2,3]])
    print(answer)