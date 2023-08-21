# Contest346, Q2


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lst_s = list(s)
        for i in range(len(lst_s)//2):
            if lst_s[i] == lst_s[-(i+1)]:
                continue
            if ord(s[i]) > ord(lst_s[-(i+1)]):
                lst_s[i] = lst_s[-(i+1)]
            else:
                lst_s[-(i+1)] = lst_s[i]

        return ''.join(lst_s)


if __name__ == "__main__":
    test = Solution()
    print(test.makeSmallestPalindrome(s = "egcfe"))
    print(test.makeSmallestPalindrome(s = "abcd"))
    print(test.makeSmallestPalindrome(s = "seven"))
