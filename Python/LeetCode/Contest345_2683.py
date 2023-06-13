# Contest345, Q2

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        tmp = [False for i in range(len(derived))]
        for i in range(len(derived)-1):
            if derived[i]:
                tmp[i+1] = not tmp[i]
            else:
                tmp[i+1] = tmp[i]

        if tmp[-1] ^ tmp[0] == derived[-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    test = Solution()
    print(test.doesValidArrayExist(derived=[1, 1, 0]))
    print(test.doesValidArrayExist(derived = [1,1]))
    print(test.doesValidArrayExist(derived = [1,0]))