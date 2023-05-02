#Contest337, Q1

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        result = [0, 0]
        str_bin_num = str(bin(n))
        # print(str_bin_num)
        for i in range(len(str_bin_num)):
            idx = i % 2
            # print(i, idx)
            if str_bin_num[-(i+1)] == '1':
                result[idx] += 1

        return result


if __name__ == '__main__':
    test = Solution()
    answer = test.evenOddBit(17)
    print(answer)
    answer = test.evenOddBit(2)
    print(answer)