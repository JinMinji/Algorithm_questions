# Contest347, Q1

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num) -1, -1, -1):
            if num[i] == '0':
                continue
            num = num[0:i+1]
            break

        return num


if __name__ == "__main__":
    test = Solution()
    print(test.removeTrailingZeros(num = "51230100"))
    print(test.removeTrailingZeros(num = "123"))