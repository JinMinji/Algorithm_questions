#Contest339, Q3

from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        gaps = []
        res = 0
        tmp = []
        for i in range(len(reward1)):
            gaps.append(reward1[1] - reward2[i])


        tmp.sort(reverse=True)
        print(tmp)
        eaten = [0 for i in range(len(reward1))]
        for i in range(len(tmp)):
            point, mouse, idx = tmp[i]
            print(point, mouse, idx, eaten, res)
            if 0 not in eaten:
                break
            if mouse == 0 and k > 0:
                if eaten[idx] == 0:
                    k -= 1
                    res += point
                    eaten[idx] = -1
                continue
            else:
                if mouse == 1 and eaten[idx] == 0:
                    res += point
                    eaten[idx] = point
                continue
        print(eaten)
        print(k, gaps)
        while k > 0:
            min_gap = min(gaps)
            cancel_idx = gaps.index(min(gaps))
            gaps[cancel_idx] = 1000
            res -= min_gap
            k -= 1
        return res


if __name__ == '__main__':
    test = Solution()
    # answer = test.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2)
    # print(answer)
    # answer = test.miceAndCheese(reward1 = [1,1], reward2 = [1,1], k = 2)
    # print(answer)
    answer = test.miceAndCheese(reward1=[2,4,2,4,2,3], reward2=[2,2,4,3,1,3], k=1)
    print(answer)