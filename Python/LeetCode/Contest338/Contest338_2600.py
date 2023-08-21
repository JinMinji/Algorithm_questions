#Contest338, Q1


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if k - numOnes <= numZeros:
            return numOnes
        return numOnes - (k-numOnes-numZeros)


if __name__ == '__main__':
    test = Solution()
    answer = test.kItemsWithMaximumSum(3, 2, 0, 2)
    print(answer)
    answer = test.kItemsWithMaximumSum(3, 2, 0, 4)
    print(answer)