# Contest351, Q2

from math import log2

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        cur = num1
        answer = 0
        for i in range(6):
        # while cur != 0:
            x = log2(cur - num2)
            print(cur, x)
            if x < 0:
                break
            if x == int(x):
                return answer + 1
            cur -= 2**int(x) + num2
            print('????cur', cur)
            answer += 1
        return -1


if __name__ == "__main__":
    test = Solution()
    print(test.makeTheIntegerZero(num1 = 3, num2 = -2))
    print(test.makeTheIntegerZero(num1 = 5, num2 = 7))
    # print(test.makeTheIntegerZero())
